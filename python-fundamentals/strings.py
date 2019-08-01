# Can be enclosed with either single or double quotes
#
# *********************************************************************************
# Best practice - use double quotes
# Avoids having to escape the apostrophe
# *********************************************************************************
#
# Can concatenate strings with +
#
# You can declare a long string with triple quotes : long_string = """
# Three dots with REPL let you know it's waiting for input, ex:
#
# >>> long_string = """
# ... 12345
# ... abc
# ... """
# >>> long_string
# '\n12345\nabc\n'
# >>>
#
# *********************************************************************************
#
# f-string was introduced in Python 3, new formatting for strings (string interpolation)
#
# ex:
# >>> name = "Nina"
# f"Hello, {name}"
# 'Hello, Nina'
#
# Could also use this way:
# print("My name is", name)
# >>> My name is Nina
#
# *********************************************************************************
#
# There is also percent formatting
# print("Hello, %s" % name)
# Hello, Nina
#
# *********************************************************************************
# You can't concatenate a string and an int, can only concat strings
# You would need to convert the int to str or str to int
# *********************************************************************************
#
