# Tuples are very similar to list but tuples can not be changed
my_tuple = ('String', 2, False, None, [1, 4, 6.897], (1, 6, 9))
hello = tuple('Hello')
empty_tuple = tuple()
empty_tuple1 = ()

tup = 1, 2, 3, 4
print(tup)
a, *b, c = tup
print(b)

# print(my_tuple, hello, empty_tuple1, empty_tuple)
# we can access tuple value by index
print(my_tuple[2])
# we can slice tuple same as list
print(my_tuple[2:4])
print(my_tuple[::-1])
# we can get index of value of tuple
print(my_tuple.index(None))
print(my_tuple.count(False))
# we can not change value of tuple
# my_tuple[0] = True
#  my_tuple[0] = True
# TypeError: 'tuple' object does not support item assignment
# BUT we can change value of list in tuple
my_tuple[4][0] = 'New String'
print(my_tuple)
my_tuple[4].append('Append string')
print(my_tuple)
# Therefore, they do not have any of the methods that can be used in lists to manipulate its contents:
#
# Append
# Extend
# Insert
# Pop
# Remove
# Sort
# Reverse

# comparing tuples
tuple1 = (1, 2, 3)
tuple2 =(1, 2, 3)
print(tuple2 == tuple1)
# print(tuple2 is tuple1)
tuple3 = tuple2[::-1]
print(tuple3 == tuple1)

# Task
# We need to have tuple with changed/removed/added item. How can we implement it in python?
my_tuple = ('String', None, 2, [1, 'B', True], True, None)

my_list = list(my_tuple)
my_list[0] = 'New String'
my_new_tup = tuple(my_list)
print(my_new_tup)
