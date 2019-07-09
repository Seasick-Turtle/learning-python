# Functions
#
# ex:
# >>> def foo():
# ...     print("Hello!")
# ...
# >>> foo()
# Hello!
#
# >>> def meaning_of_life():
# ...     return 42
# ...
# >>> meaning_of_life()
# 42
#
# >>> called_foo = foo()
# Hello!
# >>> called_foo
# >>> (nothing is shown because foo doesn't return anything)
#
# >>> x = meaning_of_life()
# >>> x
# 42
#
# example of using arguments:
#
# >>> def add_numbers(x, y):
# ...     return x + y
# ...
# >>> add_numbers(3, 5)
# 8
# >>> a = 1
# >>> b = 5
# >>> add_numbers(a, b)
# 6
#
# Should you make mistakes with declaring functions, python will assist with syntax errors
# ex:
#
# >>> def oops() <-- missing colon
#   File "<stdin>", line 1
#     def oops()
#              ^
# SyntaxError: invalid syntax
#
# Functions can be multiline, ex:
#
# >>> def greeting(name):
# ...     greeting = "Hello "
# ...     return greeting + name
#
# >>> greeting("Nina")
# 'Hello Nina
#
# You can use return statements that return no value, used in control flows
#
# >>> def foo():
# ...     x = 5
# ...     return
#
# >>> x = foo()
# >>> type(x)
# <class 'NoneType'>
#
#
# ###############################################
#
# Function Arguments
#
# >>> def add_numbers(x, y);
# ...     return x + y
#
# >>> add_numbers(3, 5)
# 8
#
# Python is helpful in letting us know what is missing
# ex:
# >>> add_numbers(3)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: add_numbers() missing 1 required positional argument: 'y'
#
# Function without default arguments:
#
# >>> def say_greeting(greeting, name):
# ...     print(f"{greeting}, {name}")
# ...
# >>> say_greeting("Hello, "Nina")
# Hello, Nina
#
# Note: If you declare a function with the same name in the REPL
# it will just overwrite the previous one
#
# Function with default arguments:
# Note: Default arguments always go last
#
# >>> def say_greeting(name, greeting="Hello"):
# ...     print(f"{greeting}, {name}")
# ...
# >>> say_greeting("Nina")
# Hello, Nina
# ^^^^^ default argument("Hello") + value passed in ("Nina")
#
# Note: If you pass in an argument, the default value is overwritten
# ex:
#
# >>> say_greeting("Nina", "Bonjour")
# Bonjour, Nina
#
# Example of how not to use default arguments:
# >>> def say_greeting_bad(greeting="Hello", name):
# ...     print(name)
# ...
#   File "<stdin>", line 1
# SyntaxError: non-default argument follows default argument (wrong order)
#
# You can ;
# >>> def create_query(language="Javascript", num_stars=50, sort="desc"):
# ...     return f"language: {language}, {num_stars} {sort}"
# ...
# >>> create_query()
# 'language: Javascript, 50 desc'
# >>> create_query(language="Python")
# 'language: Python, 50 desc'
# >> create_query(language="Python", sort=100, num_stars=1)
# 'language: Python, 1 100'
#
# >>> def foo(a, b=5):
# ...     return a + b
# ...
# >>> foo(3)
# 8
#
# >>> foo(3, b=6)
# 9
#
# If you want to be explicit, you can pass in a value to the argument a
#
# >>> foo(a=3, b=7)
# 10
#
