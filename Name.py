Python 3.13.1 (v3.13.1:06714517797, Dec  3 2024, 14:00:22) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # A simple program to greet the user
... name = input("Enter your name: ")
... print(f"Hello, {name}! Welcome to GitHub!")
... 
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> name = input("Enter your name: ")
Enter your name: Curtis
>>> name
'Curtis'
>>> name
'Curtis'
>>> print(f"{name})
...       
SyntaxError: unterminated f-string literal (detected at line 1)
>>> print(f"{name}")
...       
Curtis
>>> name
...       
'Curtis'
