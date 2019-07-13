# Lists
#
# Lists are used for storing similar items and in cases where
# items need to be added ro removed
#
# Lists can hold primitive types and more advanced data types
# Items in a list don't have to be of the same data type
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
# ######################################
#
# Looking for an item in a list
#
# Looking for an item is a slow operation as it checks every value
# There are multiple ways of doing so
# Here is using the in keyword:
#
# >>> names = ['Nina', 'Max', 'Phillip', 'Nina']
# >>> 'Rose' in names
# False
# >>> 'Nina' in names
# True
#
# You can use the index method of a list to find the first result
#
# >>> names.index('Max')
# 1
# >>> names.index('Nina')
# 0
#
# If you want to find out how many times an item
# appears in a list, use the count method
#
# >>> names.count('Max')
# 1
# >>> names.count('Nina')
# 2
#
# You can use .index with to assist with updating items
# in a list
#
# >>> names[0] = 'Jimmy'
# >>> names
# ['Jimmy', 'Max', 'Phillip', 'Nina']
# >>> pos = names.index('Phillip')
# >>> names[pos] = 'Floyd'
# >>> names
# ['Jimmy', 'Max', 'Floyd', 'Nina]
#
# #################################################
#
# Removing items from a list
#
# There are several methods of doing so, just like insert
# Using .remove removes the first item from the list:
#
# >>> names = ['Nina', 'Max']
# >>> names.remove('Max')
# >>> names
# ['Nina']
# >>> names = ['Nina', 'Max', 'Nina']
# >>> names.remove('Nina')
# >>> names
# ['Max', 'Nina']
#
# You can use the pop method to remove an item at the end
# of the list or use it with an index to remove an
# item at particular position, it'll also return the
# item that was just removed
#
# >>> names
# ['Max', 'Nina']
# >>> names.pop()
# 'Nina' <-- item that was popped
# >>> names
# ['Max']
#
# >>> names = ['Nina', 'Rose', 'Max']
# names.pop(1)
# 'Rose'
# >>> names
# ['Nina', 'Max']
#
