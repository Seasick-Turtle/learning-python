# Functions
#
# Format of creating a function
# ex:
# >>> def foo():
# ...     print("Hello!")
# ... (<-- hitting enter twice in the REPL to create this whitespace)
# >>> foo()
# Hello!
#
# *********************************************************************************
# Note: be sure to indent, otherwise you'll receive an indentation error
# Also, x and y are known as positional arguments
# *********************************************************************************
#
# >>> def add_numbers(x, y):
# ... return x + y
#   File "<stdin>", line 2
#     return x + y
# IndentationError: expected an indented block
#
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
# *********************************************************************************
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
# *********************************************************************************
# Note: If you declare a function with the same name in the REPL
# it will just overwrite the previous one
# *********************************************************************************
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
#
#
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
# *********************************************************************************
# If you want to be explicit, you can pass in a value to the argument a
# *********************************************************************************
#
# >>> foo(a=3, b=7)
# 10
#
# It is recommended to not use mutable arguments as default arguments
# such as a list because that value is instantiated only the FIRST TIME
# the function is called and then that value is shared
# ex:
#
# >>> def foo(a, b=[]):
# ...     b.append(a)
# ...     print("B is: ", b)
# ...
# >>> foo(5)
# B is: [5]
# >>> foo(6)
# B is: [5, 6]
#
# *********************************************************************************
#
# Function Scope in Python
#
# Python scoping happens with whitespace
# The block of indented code for the function changes into
# the internal scope of that particular function
#
# The function scope has access to external variables but can't change them
# ex:
#
# >>> def twitter_info():
# ...     account = "nnja"
# ...     print(f"Account inside the function is: {account}")
# ...
# >>> twitter_info()
# Account inside the function is: nnja
# >>> account
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'account' is not defined
#
# >>> name = "Nina"
# >>> def try_change_name():
# ...     name = "Max"
# ...     print(f"Name inside function: {name}")
# >>> try_change_name()
# Name inside function: Max
# >>> f"Name outside of the function: {name}"
# 'Name outside of the function: Nina
#
# *********************************************************************************
#
# Generally, in production you don't want a lot of variables floating around
# outside of a defined scope, constants however are generally okay
#
# Don't do this:
# source of bugs
#
# Do not use empty lists as arguments, default arguments get instantiated once
# which is when the function is defined, primitives are safe to use
# >>> def foo(a, b=[]):
# ...     b.append(a)
# ...     print(b)
# ...
# >>> foo(1)
# [1]
# >>> foo(5)
# [1, 5]
#
# Do this instead
#
# >>> def foo(a, b=None):
# ...     if b is None:
# ...             b = []
# ...     b.append(a)
# ...     print(b)
# ...
# >>> foo(1)
# [1]
# >>> foo(5)
# [5]
#
# Keyword arguments are for setting default values, these are optional and must always come
# after any positional arguments, example:
#
# >>> def calculate_numbers(x, y, operation="add"):
# ...     if operation == "add":
# ...         return x + y
# ...     elif operation == "subtract";
# ...          return x - y
# ...
#
# If we don't pass a value to the keyword argument, we get the default of "add"
# >>> calculate_numbers(2, 3)
#
# You can pass a keyword argument as a normal positional argument
# >>> calculate_numbers(2, 3, "subtract")
#
# You can also use the argument's keyword, this helps with readbility
# >>> calculate_numbers(2, 3, operation="subtract")
#
