# Review task: import_integrity_check.py

You are ChatGPT-5.5, reviewing this Python tool for correctness. Be critical.

## The tool

Located at: <PROJECT_ROOT>/import_integrity_check.py

It's a static import dependency checker for Python projects. It should:
1. Recursively find all .py files
2. Extract all import/from statements via ast.parse
3. Check if imported modules exist as .py files or packages in the target dir or sys.path
4. Report missing modules with source file locations
5. Exit 0 if all ok, exit 1 if missing imports found

## Review questions

1. **Correctness**: Are there bugs in the import resolution logic? Does `is_resolvable()` handle all cases correctly? What about `sys.path` handling — does iterating over `sys.path` at module level capture the right paths?
2. **False positives**: What legitimate imports would this falsely flag as missing? Consider: relative imports within a package, namespace packages, builtin-only modules, C extensions, modules installed via pip but not in sys.path at check time.
3. **False negatives**: What truly missing imports would this MISS? Consider: dynamic imports, optional dependencies in try/except, conditional imports.
4. **Implementation bugs**: Any Python errors? Encoding issues on Windows? Path handling bugs?
5. **The `builtins` edge case**: Small_Scale testing_utils.py does `import builtins` — would this tool correctly handle it?
6. **Improvements**: What's missing that would make this a production-quality tool?

## Output

Write your review to:
<PROJECT_ROOT>/codex_review_import_checker.md

Be concise but thorough. If you find bugs, propose fixes.
