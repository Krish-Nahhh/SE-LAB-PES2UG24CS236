# Reflection

### 1. What did you learn from static code analysis?

I learned that static analysis tools can identify code quality, formatting, error-handling, and security issues without executing the program. Pylint checks code quality, Flake8 checks style and formatting, and Bandit identifies potential security vulnerabilities.

### 2. What were the major issues identified?

The tools identified unsafe use of eval(), weak MD5 hashing, shell command execution, a bare exception handler, and a mutable default argument. They also reported unused variables, missing docstrings, and formatting problems.

### 3. How were the issues fixed?

I replaced eval() with direct arithmetic, changed MD5 to SHA-256, removed shell command execution, added explicit handling for missing patient IDs, and replaced the mutable default list with None. I also improved function documentation and code formatting.

### 4. What did you learn about secure and maintainable programming?

I learned that code can produce the expected output while still containing security vulnerabilities and maintainability problems. Using static analysis tools helps detect these issues early and encourages safer, more readable, and more reliable code.
