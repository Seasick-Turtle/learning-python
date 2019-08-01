# Tuples
#
# *********************************************************************************
#
# Used to keep track of related but different items
# Tuples are immutable, once created the items in it can't change
#
# Comparison: lists are used to store collections of similar
# items together while tuples can be considered to contain a snapshot
# of data. They can't be continually changed, added, or removed like
# in a list
#
# example:
#
# >>> a = ()
# >>> type(a)
# <class 'tuple'>
#
# *********************************************************************************
#
# tuple with one value (tuples are not just parentheses, they're also commas)
# Without comma:
# >>> b = (1)
# >>> type(b)
# <class 'int'>
#
# >>> c = (1,)
# >>> type(c)
# <class 'tuple'>
#
# >>> student = ("Marcy", 8, "History", 3.5)
# >>> student[0]
# 'Marcy'
# >>> student[1]
# 8
#
# Tuples don't allow item assignment
# >>> student[0] = "Nina"
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment
#
# *********************************************************************************
# You can't use a mutable data type as a key in data structures like a dictionary
# *********************************************************************************
#
# Tuples are a great way to consolidate information due to tuple unpacking
#
# >>> student
# ('Marcy', 8, 'History', 3.5)
# >>> name, age, subject, gpa = student
# >>> name
# 'Marcy'
# >>> age
# 8
# >>> subject
# 'History
# >>> gpa
# 3.5
#
# When unpacking, be sure to have the correct number of variables
# ex:
#
# >>> foo, bar, baz = student
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: too many values to unpack (expected 3)
#
# *********************************************************************************
# If you don't want to save a value when unpacking use an underscore
# *********************************************************************************
#
# >>> name, age, subject, _ = student
#
# *********************************************************************************
# Quick Note: You can declare a tuple without the parentheses
#
# >>> x = 1, 2, 3
# type(x)
# <class 'tuple'>
# *********************************************************************************
#
# You can return tuples from functions and use unpacking
#
# >>> def http_status_code():
#          return 200, "OK"
#
# >>> http_status_code()
# (200, 'OK')
# >>> code, name = http_status_code()
# >>> code
# 200
# >>> name
# 'OK'
#
# *********************************************************************************
#
# You can search a tuple using .index(item) or item in
# ex: my_tuple.index(item) or item in my_tuple
#
