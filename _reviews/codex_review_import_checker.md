# Critical review: `import_integrity_check.py`

## Verdict

The checker is useful only for the simplest case: top-level, pure-Python modules in a flat project root. It is not reliable enough as a release gate for Python import integrity. The current implementation will both flag valid imports as missing and miss genuinely broken imports.

A direct run in this workspace already proves a core bug:

```text
python import_integrity_check.py .
```

reported `sys` as unresolved, even though `sys` is a builtin module. On this Windows shell the output separator also rendered as mojibake (`[sys] ... imported`), which confirms a console encoding portability issue.

## High-severity correctness bugs

### 1. `is_resolvable()` does not model Python import resolution

Lines 53-70 manually check only:

- `<target_dir>/<module>.py`
- `<target_dir>/<module>/__init__.py`
- the same two forms under each `sys.path` entry

That is not Python's import machinery. It misses valid modules loaded as:

- builtins: `sys`, `builtins`, `time`, `itertools`
- frozen stdlib modules
- C extension modules: `.pyd` on Windows, `.so` on Linux/macOS
- namespace packages without `__init__.py` (PEP 420)
- modules inside zip/egg importers
- modules resolved by custom `sys.meta_path`/path hooks

Result: many false positives.

The `builtins` edge case is definitely broken. `import builtins` will be reported missing unless a local `builtins.py` happens to exist, because `builtins` is not represented as `builtins.py` or `builtins/__init__.py` on disk.

Suggested fix: use Python's import machinery instead of hand-rolled file probing. At minimum:

```python
import importlib.util

def is_resolvable(module_name: str, target_dir: Path) -> bool:
    if module_name in sys.builtin_module_names:
        return True
    if hasattr(sys, "stdlib_module_names") and module_name in sys.stdlib_module_names:
        return True

    # Search target_dir as an import root.
    old_path = sys.path[:]
    try:
        sys.path.insert(0, str(target_dir.resolve()))
        return importlib.util.find_spec(module_name) is not None
    finally:
        sys.path[:] = old_path
```

For production, prefer a resolver that accepts configured import roots and does not rely on mutating process-global `sys.path`.

### 2. The checker records only the top-level import name

Lines 46 and 49 use `split(".")[0]`. This creates serious false negatives.

Examples:

```python
import pkg.missing_submodule
from pkg.missing_submodule import X
```

If `pkg` exists, the checker marks both imports as valid even when `pkg.missing_submodule` does not exist. Python would fail at runtime.

This also loses meaningful diagnostics: the report says only `pkg`, not the actual missing path.

Suggested fix: preserve the full imported module path for `import a.b.c` and `from a.b.c import X`. Check the longest module path first, then fall back carefully for ambiguous forms like `from pkg import name`, where `name` may be either a submodule or an attribute exported by `pkg.__init__`.

### 3. Relative imports are mishandled

`ast.ImportFrom` has a `level` field. The script ignores it.

Broken cases:

```python
from . import sibling
from .sibling import value
from ..common import helper
```

Current behavior:

- `from . import sibling`: `node.module` is `None`, so the import is silently ignored. That is a false negative if `sibling.py` is missing.
- `from .sibling import value`: the checker records `sibling` as a top-level module. That can be either a false positive or a false negative, depending on whether a top-level `sibling.py` exists.
- `from ..common import helper`: the checker records `common` as top-level, not package-relative.

Suggested fix: compute the importing file's package context from its path and surrounding `__init__.py` files, then resolve `node.level` and `node.module` to the intended absolute module path. If package context cannot be determined, report the import as indeterminate instead of pretending it is top-level.

### 4. `sys.path` is the checker process's environment, not the target project's environment

Lines 63-69 iterate over the `sys.path` of the Python process running the checker. That may not match the project being checked.

False positives:

- dependency is installed in the target project's virtualenv but the checker is run with the wrong interpreter
- project uses `src/` layout and `src` is not on `sys.path`
- project needs configured extra import roots

False negatives:

- dependency exists in the developer's global interpreter but is absent from the target deployment environment
- dependency is importable locally but missing from `pyproject.toml`/`requirements.txt`
- checker script directory is on `sys.path`, so unrelated local files can satisfy imports for the wrong project

Suggested fix: make the runtime environment explicit. Options:

- require running inside the target venv and document that requirement
- support `--python` to query a target interpreter
- support `--path`/`--src-root`
- optionally compare imports against declared dependencies in `pyproject.toml` or requirements files

## False positives

Legitimate imports this tool can incorrectly report as missing:

- `import sys`
- `import builtins`
- C extensions such as `_ssl`, `_socket`, `_sqlite3`, or third-party single-file `.pyd` modules
- frozen stdlib modules
- namespace packages with no `__init__.py`
- imports inside optional dependency guards:

```python
try:
    import rich
except ImportError:
    rich = None
```

- imports inside platform guards:

```python
if sys.platform == "win32":
    import winreg
```

- imports inside `if TYPE_CHECKING:` blocks
- relative imports inside packages
- packages available only through configured `PYTHONPATH`, editable installs, zip imports, or a target virtualenv

The optional dependency limitation is mentioned in the docstring, but the current output does not distinguish "hard missing" from "optional/conditional/type-checking only", so the report will be noisy.

## False negatives

Broken imports this tool can miss:

- missing submodules under an existing top-level package:

```python
import existing_pkg.missing
from existing_pkg.missing import Thing
```

- missing relative imports with `from . import missing`, because `node.module` is `None`
- broken relative imports that accidentally match an unrelated top-level module
- dynamic imports:

```python
import importlib
importlib.import_module("missing_plugin")
__import__("missing_backend")
```

- imports assembled from strings, config, entry points, plugin registries, or framework conventions
- imports that work on the checker's machine only because an undeclared dependency is globally installed
- files with syntax errors are skipped, so their imports are not checked at all

Conditional imports are mixed: the checker will report static conditional imports even when they are optional, but it cannot know whether a guarded import is mandatory for a supported feature. A production checker should classify these separately rather than treating every AST import as the same severity.

## Windows and encoding issues

Line 38 uses:

```python
filepath.read_text(encoding="utf-8")
```

Python source files are not always raw UTF-8 text read this way. PEP 263 allows source files to declare an encoding, for example `# -*- coding: cp1252 -*-`. `ast.parse()` on a decoded string will not detect that encoding cookie. On Windows, legacy code pages and GBK/CP936 files are common enough that this can abort a scan.

Also, only `SyntaxError` is caught. `UnicodeDecodeError` or `OSError` will crash the whole tool.

Suggested fix:

```python
import tokenize

try:
    with tokenize.open(filepath) as f:
        source = f.read()
    tree = ast.parse(source, filename=str(filepath))
except (SyntaxError, UnicodeDecodeError, OSError) as e:
    ...
```

Console output also uses a Unicode dash on line 111. In this Windows run it rendered incorrectly. Use ASCII output for a portable CLI, or configure stdout explicitly:

```python
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
```

ASCII is simpler and more robust for this script.

## Other implementation issues

- `os` is imported but unused.
- `candidate_py.exists()` should be `is_file()`; a directory named `foo.py` would currently count.
- the recursive scan has no excludes for `.venv`, `venv`, `.tox`, `build`, `dist`, or generated directories
- `target_dir` is not normalized with `resolve()`, which can make relative path reporting and containment checks fragile
- the checker reports only the first five source locations per module, which is fine for CLI readability but weak for machine-readable CI output
- it has no JSON output for CI or follow-up automation

## Recommended production direction

Do not try to patch this by adding one-off checks for `sys` and `builtins`. The core issue is that the script reimplements import resolution incorrectly.

A better design:

1. Parse files with `tokenize.open()`.
2. Preserve full import names and `ImportFrom.level`.
3. Build configured project import roots, including common `src/` layout.
4. Resolve local package-relative imports explicitly.
5. Use `importlib.util.find_spec()` or `importlib.machinery.PathFinder` for real importability checks.
6. Treat builtins, frozen modules, stdlib modules, namespace packages, and extension modules as resolvable.
7. Classify imports by context: unconditional, try/except optional, `TYPE_CHECKING`, platform-gated, function-local.
8. Provide ignore/config support for optional dependencies and plugin systems.
9. Add JSON output and tests with fixtures for flat modules, packages, relative imports, namespace packages, `src/` layout, builtins, extension modules, and non-UTF-8 source files.

Until those changes exist, this script should be described as a best-effort smoke check for simple repositories, not an import integrity checker suitable for release validation.
