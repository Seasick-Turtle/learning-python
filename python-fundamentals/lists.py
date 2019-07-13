# Lists
#
# Lists are used for storing similar items and in cases where
# items need to be added ro removed
#
# Can be created with empty brackets [] or with a variable
# >>> type([])
# <class 'list'>
#
# names = ['Nina', 'Max', 'Rose']
# >>> type(names)
# <class 'list'>
# >>> names
# ['Nina', 'Max', 'Rose']
# >>> print(names)
# ['Nina', 'Max', 'Rose']
#
# You can use the len built in method to find the length
# of the list (this is a globally available method)
#
# Lists retain the order of items in them, in order to
# access the items in the list you need to use the proper
# index
#
# ex:
#
# >>> my_list = ['a','b', 'c']
#   (index pos)   0   1    2
# >>>  len(my_list)
# 3
# >>> my_list[1]
# b
# >>> my_list[0]
# a
# >>> my_list[2]
# c
#
# To update a partiular item:
# >>> names
# ['Nina', 'Max', 'Rose']
# >>> names[1] = 'Jimmy'
# names
# ['Nina', 'Jimmy', 'Rose']
#
# You can also do this:
# >>> names = [
# ... 'Nina',
# ... 'Jimmy',
# ... 'Rose, (<-- you can leave a trailing comma for future purposes)
# ... ]
# >>> names
# ['Nina', 'Jimmy', 'Rose']
#
# You can sort two ways in Python
# The first being with the sorted method, ex:
#
# >>> lottery_numbers = [1, 4, 34242, 78, 11]
# >>> sorted(lottery_numbers) (<-- the sorted method returns a copy of the list)
# [1, 4, 11, 78, 34242]
# >>> lottery_numbers
# [1, 4, 34242, 78, 11]
#
# The sorted method also takes an optional argument
# >>> sorted(lottery_numbers, reverse=True)
# [34242, 78, 11, 4, 1]
# >>> lottery_numbers
# [1, 4, 34242, 78, 11]
#
# However you can always save the results of the sorted method
# with the use of a variable, ex:
#
# >>> x = sorted(lottery_numbers)
# >>> x
# [1, 4, 11, 78, 34242]
#
# The second way of sorting lists in Python which changes
# the list itself by using the sort method
#
# >>> lottery_numbers.sort()
# >>> lottery_numbers
# [1, 4, 11, 78, 34242]
#
# If we wanted to sort it in reverse, use the .reverse method
# >>> lottery_numbers.reverse()
# >>> lottery_numbers
# [34242, 78, 11, 4, 1]
#
# Note: If you forget what is availble to lists, use dir(list)
#
# Additional: if you forget what arguments the method use, do this:
# >>> help(list.reverse) leave out the parentheses at the end, just use type and method
#
# Which will return:
#
# Help on method_descriptor:
#
# reverse(self, /)
#   Reverse *IN PLACE*
# (END)
#
# ###########################################
#
# Adding items to a list
#
# >>> names = ['Nina', 'Max']
#
# To add to the end of the list above, we use .append
#
# >>> names.append('Jimmy')
# >>> names
# ['Nina', 'Max', 'Jimmy']
# >>> len(names)
# 3
#
# We can also use the insert method to put an item
# in a specific position
#
# insert into listt == my_list(pos, value)
#
# >>> names.insert(0, 'Rose')
# >>> names
# ['Rose', 'Nina', 'Max', 'Jimmy']
#
# Another way of adding to a list is by attaching another list
# using the extends method, ex:
#
# >>> names = ['Nina', 'Max']
# >>> colors = ['Red', 'Blue']
# >>> names.extend(colors)
# >>> names
# ['Nina', 'Max', 'Red', 'Blue']
#
