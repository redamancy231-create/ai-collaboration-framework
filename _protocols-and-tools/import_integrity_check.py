#!/usr/bin/env python3
"""Import integrity checker -- static analysis of Python import dependencies.

Finds modules imported but not present in the repository or Python environment.
Use before publishing/releasing a Python project.

Usage:
    python import_integrity_check.py [target_dir] [--json]

Output:
    Lists missing modules with their importing files.
    Exit code 0 = all imports resolvable.
    Exit code 1 = unresolved imports found.

Limitations:
    - Does not handle dynamic imports (importlib, __import__).
    - Optional dependencies may trigger false positives.
    - Not a replacement for a minimal end-to-end smoke test.
    - Run inside the target project's virtualenv for accurate results.
"""

import ast
import importlib.util
import json
import sys
import tokenize
from pathlib import Path
from collections import defaultdict

# Directories to skip during recursive scan
SKIP_DIRS = {
    ".git", ".venv", "venv", ".tox", ".nox",
    "__pycache__", "build", "dist", "eggs",
    ".eggs", "node_modules", ".mypy_cache",
    ".pytest_cache", ".ruff_cache",
}


def find_py_files(root: Path) -> list[Path]:
    """Recursively find all .py files under root, skipping generated dirs."""
    py_files = []
    for entry in sorted(root.rglob("*.py")):
        if any(skip in entry.parts for skip in SKIP_DIRS):
            continue
        py_files.append(entry)
    return py_files


def read_source(filepath: Path) -> str | None:
    """Read and decode a Python source file using PEP 263 encoding detection."""
    try:
        with tokenize.open(str(filepath)) as f:
            return f.read()
    except (SyntaxError, UnicodeDecodeError, OSError) as e:
        print(f"  [SKIP] Cannot read {filepath}: {e}")
        return None


def extract_imports(filepath: Path) -> list[tuple[str, int, str, int | None]]:
    """Extract (full_module_name, lineno, import_type, level) from a Python file.

    import_type: "import" | "from"
    level: None for absolute imports, 0/1/2 for relative imports (from . / from ..)
    """
    imports = []
    source = read_source(filepath)
    if source is None:
        return imports

    try:
        tree = ast.parse(source, filename=str(filepath))
    except SyntaxError as e:
        print(f"  [SKIP] Syntax error in {filepath}: {e}")
        return imports

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.append((alias.name, node.lineno, "import", None))
        elif isinstance(node, ast.ImportFrom):
            if node.level is not None and node.level > 0:
                # Relative import -- compute absolute path from file location
                if node.module:
                    abs_name = _resolve_relative(filepath, node.level, node.module)
                    imports.append((abs_name, node.lineno, "from", node.level))
                # else: ``from . import X`` -- X is a name, not a module; skip
            elif node.module:
                imports.append((node.module, node.lineno, "from", 0))

    return imports


def _resolve_relative(filepath: Path, level: int, module: str) -> str:
    """Resolve a relative import to an absolute dotted module name.

    e.g. filepath = pkg/sub/inner.py, level=2, module="common" -> "pkg.common"
    """
    # Determine the package of the importing file
    parts = list(filepath.relative_to(filepath.anchor).parts)
    # Remove filename, walk up by `level` package dirs
    if parts[-1].endswith(".py"):
        parts = parts[:-1]  # remove filename
    # Remove __init__.py directories equivalent
    parts = [p for p in parts if p != "__init__.py"]
    # Walk up `level` levels
    if level > len(parts):
        return f"<relative:{'.' * level}.{module}>"  # beyond top-level package
    base = parts[: -level] if level > 0 else parts
    if module:
        return ".".join(base + [module])
    return ".".join(base)


def is_resolvable(module_name: str, target_dir: Path) -> bool:
    """Check if module_name is importable using Python's import machinery.

    Uses importlib.util.find_spec() which correctly handles:
    - builtins (sys, builtins, time, ...)
    - frozen stdlib modules
    - C extensions (.pyd, .so)
    - namespace packages (PEP 420, no __init__.py needed)
    - regular .py files and packages
    """
    # Builtins are always available
    if module_name in sys.builtin_module_names:
        return True

    # Check if the module can be found by Python's import system
    # Temporarily prepend target_dir to sys.path for resolution
    old_path = sys.path[:]
    try:
        sys.path.insert(0, str(target_dir.resolve()))
        spec = importlib.util.find_spec(module_name)
        return spec is not None
    except (ValueError, ImportError, ModuleNotFoundError):
        return False
    finally:
        sys.path[:] = old_path


def check_imports(target_dir: Path) -> dict[str, list[tuple[Path, int, str]]]:
    """Check all Python files in target_dir for unresolvable imports."""
    py_files = find_py_files(target_dir)
    all_imports: dict[str, list[tuple[Path, int, str]]] = defaultdict(list)

    for f in py_files:
        for mod, lineno, itype, _level in extract_imports(f):
            all_imports[mod].append((f, lineno, itype))

    missing = {}
    for mod, sources in sorted(all_imports.items()):
        if not is_resolvable(mod, target_dir):
            missing[mod] = sources

    return missing


def output_text(missing: dict, target_dir: Path) -> None:
    """Human-readable text output."""
    if not missing:
        print("  All imports resolvable.")
        return

    print(f"\n  Unresolved imports: {len(missing)} module(s)\n")
    for mod, sources in sorted(missing.items()):
        print(f"  [{mod}] -- imported by {len(sources)} file(s):")
        for f, lineno, itype in sources[:5]:
            try:
                rel = f.relative_to(target_dir)
            except ValueError:
                rel = f
            print(f"      {rel}:{lineno} ({itype})")
        if len(sources) > 5:
            print(f"      ... and {len(sources) - 5} more")


def output_json(missing: dict, target_dir: Path) -> None:
    """Machine-readable JSON output."""
    result = {
        "target": str(target_dir.resolve()),
        "missing_count": len(missing),
        "missing": {}
    }
    for mod, sources in sorted(missing.items()):
        result["missing"][mod] = [
            {"file": str(f), "lineno": lineno, "type": itype}
            for f, lineno, itype in sources
        ]
    json.dump(result, sys.stdout, indent=2, ensure_ascii=False)
    print()


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--json")]
    use_json = "--json" in sys.argv

    target = Path(args[0]) if args else Path.cwd()
    target = target.resolve()

    if not target.is_dir():
        print(f"Error: {target} is not a directory")
        sys.exit(2)

    print(f"Scanning: {target}")
    py_files = find_py_files(target)
    print(f"  Found {len(py_files)} .py files")

    missing = check_imports(target)

    if use_json:
        output_json(missing, target)
    else:
        output_text(missing, target)

    if missing:
        print(f"\n  Summary: {len(missing)} module(s) not found")
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
