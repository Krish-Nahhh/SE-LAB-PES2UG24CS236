# Reflection

### 1. What did you learn from static code analysis?

I learned that static analysis tools can find code quality, formatting, error-handling and security problems without running the program. Pylint checks code quality and missing documentation, Flake8 checks PEP 8 style, and Bandit looks for security vulnerabilities. They work best together because each one catches things the others miss. I also learned that the tools are not enough on their own: the program printed a billing amount of `1344.0000000000002`, which none of them flagged, so I still had to run the program and read its output.

### 2. What were the major issues identified?

The most serious were unsafe use of `eval()`, weak MD5 hashing, shell command execution through `os.system()`, and a hardcoded `nurse_access_key` secret in the source. Medium and low issues included a bare `except` that silently ignored errors, a mutable default argument, weak random token generation, and unused variables. The tools also reported missing docstrings, bad indentation, extra blank lines, over-long lines, trailing whitespace and a missing final newline.

### 3. How were the issues fixed?

I replaced `eval()` with direct arithmetic, switched MD5 to SHA-256, removed the shell command, and replaced `random.randint()` with `secrets.randbelow()`. I replaced the bare `except` with an explicit check that reports a missing patient ID, and changed the mutable default list to `None`. I removed the unused hardcoded access key and other unused variables, added a docstring to the module and every function, and reformatted the file to PEP 8. I also rounded the treatment cost to 2 decimal places to fix the floating-point output. After these changes Pylint scored 10.00/10 (up from 7.21), Flake8 reported no warnings, Bandit reported no issues, and the program still produces the same results.

### 4. What did you learn about secure and maintainable programming?

Code can give the expected output and still contain security vulnerabilities and maintainability problems. A secret stored in source code is a risk even if it is never used, and a function like `eval()` or `os.system()` can be dangerous long before anyone attacks it. Docstrings, consistent formatting and clear error handling make code easier to read and review. Running static analysis early and after every change catches these problems cheaply, but it should be combined with testing and reading the real output.