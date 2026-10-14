# Issues Found 

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Unsafe use of `eval()` | Security - Medium | 40 | Evaluates a dynamically supplied expression, which could execute arbitrary code. | Replace `eval()` with a safe calculation method that accepts only permitted operations. |
| Weak MD5 hashing | Security - High | 45 | MD5 is unsuitable for security-sensitive hashing because it is vulnerable to collision attacks. | Use SHA-256 if a cryptographic hash is required. |
| Shell command execution | Security - High | 56 | `os.system()` executes a shell command containing a filename, creating potential command-injection risk. | Remove the shell command or use a safer alternative that does not invoke a shell. |
| Bare `except` with `pass` | Error handling - Low | 21–25 | Catches every exception and silently ignores errors, making failures difficult to detect. | Catch the specific exception, such as `KeyError`, and handle it explicitly. |
| Weak random-number generation | Security - Low | 49 | `random.randint()` is not intended for security-sensitive tokens. | Use `secrets.randbelow()` if the ward token must be unpredictable. |
| Dangerous mutable default argument | Code quality | 13 | `intake_log=[]` reuses the same list across calls that omit the argument. | Use `None` as the default and create a new list inside the function. |
| Unused variables | Code quality | 29, 39 | `bed_charge` and `base_bill` are assigned but not used as intended. | Remove unnecessary variables or use them in the calculations. |
| Missing final newline | Style | 80 | The Python file does not end with a newline. | Add a newline at the end of the file. |

