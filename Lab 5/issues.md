# Issues Found


| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Shell command execution | Security - High | 56 | `os.system()` executes a shell command containing a filename, creating potential command-injection risk. | Remove the shell command or use a safer alternative that does not invoke a shell. |
| Weak MD5 hashing | Security - High | 45 | MD5 is unsuitable for security-sensitive hashing because it is vulnerable to collision attacks. | Use SHA-256 if a cryptographic hash is required. |
| Unsafe use of `eval()` | Security - Medium | 40 | Evaluates a dynamically supplied expression, which could execute arbitrary code. | Replace `eval()` with direct arithmetic that accepts only permitted operations. |
| Hardcoded secret (`nurse_access_key`) | Security - Medium | 74 | A master key is stored in plain text in source code and never used, so it would leak through version control. | Remove it; if a key is ever needed, load it from an environment variable or secrets manager. |
| Weak random-number generation | Security - Low | 49 | `random.randint()` is not intended for security-sensitive tokens. | Use `secrets.randbelow()` for the ward token. |
| Bare `except` with `pass` | Error handling - Low | 21-25 | Catches every exception and silently ignores errors, making failures difficult to detect. | Check whether the ID exists and report a clear "not found" message instead. |
| Dangerous mutable default argument | Code quality | 13 | `intake_log=[]` reuses the same list across calls that omit the argument. | Use `None` as the default and create a new list inside the function. |
| Floating-point rounding in billing | Logic / output bug | 45 | `calculate_treatment_cost("P103")` printed `1344.0000000000002` because 1200.0 × 1.12 is not exact in binary floating point. No tool flags this. | Return `round(base_bill * 1.12, 2)`. |
| Unused variables | Code quality | 29, 39, 74 | `bed_charge`, `base_bill` and `nurse_access_key` are assigned but not used as intended (Pylint W0612, Flake8 F841). | Remove unnecessary variables or use them in the calculations. |
| Missing docstrings | Code quality | 1, 13, 39, 52, 55, 59, 66, 73 | The module and seven functions have no docstrings (Pylint C0114, C0116). | Add a short docstring to the module and every function. |
| Formatting and PEP 8 violations | Style | 6-9, 39, 44, 52, 55, 66, 67, 70, 83 | Extra blank lines (E303), missing blank lines (E302), lines over 79 characters (E501), space before `)` (E202), 5-space indentation (E111/E117/W0311), bad continuation line (E122) and trailing whitespace (W293/C0303). | Reformat to PEP 8: two blank lines between functions, 4-space indents, wrapped long lines, no trailing whitespace. |
| Missing final newline | Style | 80, 86 | The Python file does not end with a newline (W292/C0304). | Add a newline at the end of the file. |

## Final tool results after fixes

| Tool | Before | After |
|---|---|---|
| Pylint | 7.21/10 | 10.00/10 |
| Flake8 | 15 warnings | 0 warnings |
| Bandit | No issues | No issues |