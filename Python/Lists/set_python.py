# Sets distinctive feature is that they do not allow duplicate values.
#
# They:
# Have no order.
# Do not store duplicate values.
# Do not allow their objects to be changed.
# Allow objects of different types.

my_set = {'String', 2, (True, False, None), 4.786}
hello = set('Hello')
print(hello)
empty_set = set()
print(empty_set)
# But the items themselves can not be sets list or dict

# A set can also be created using the copy method of another set.
new_set = my_set.copy()
print(new_set)
#  We can not access values in set using index
# print(my_set[1]) -> TypeError
# Therefore, there is no index method. Because the set has no order, it has no method sort or reverse. And because the
# set has no repeated values, it does not have the count method either.

# We can add value to set
my_set.add('New String')
my_set.update(['Banana', 'Apple', 'Apple'])
print(my_set)

random = my_set.pop()  # in case with set it will remove random item and return it, we can not pass parameter
print(random)
print(my_set)
# The discard method removes the given value and returns nothing.
my_set.discard('New String')
print(my_set)
# my_set.remove('New String')  # remove method will give KeyError if item do not found
test_set = {1, '2', 3.67}
print(test_set)
test_set.clear()
print(test_set)


fruits = {"Pear", "Mango", "Apple", "Strawberry"}
smoothie = {'Mango', 'Orange', 'Pear'}
# The method intersection returns a set containing the values present in both sets. The original sets remain unchanged.
print(fruits.intersection(smoothie))
# The method difference returns a set containing the values present in A that don’t exist in B. The original sets
# remain unchanged.
print(fruits.difference(smoothie))
# The method symmetric_difference returns a set containing the values present in A or B that don’t exist at the same
# time in both. The original sets remain unchanged.
print(fruits.symmetric_difference(smoothie))

# The difference_update, intersection_update and symmetric_difference_update methods will calculate the same thing as
# do the difference, intersection and symmetric_difference methods.
# The difference is that the first methods will overwrite the original set (fruits, in this case) instead of returning
# the result.
# The method union returns a set containing the values present in A or B (or both). The original sets remain unchanged.
union_fruits = fruits.union(smoothie)
print(union_fruits)

# The previous methods return a set with the result. Sometimes the script only requires to know if some kind of
# relationships exists between the sets, not the particular values.
#
# The method isdisjoint returns True if the two sets have no item in common and False if they share at least one value.
print(fruits.isdisjoint(smoothie))
set1 = {1, 10, 30}
print(fruits.isdisjoint(set1))
# The method issubset returns True if the first set is completely contained in the set passed as argument.
smoothie = {'Mango', 'Pear'}
print(fruits.issubset(smoothie))
print(smoothie.issubset(fruits))

# comparing sets
set1 = {1, 2, 3}
set2 = {1, 2, 3}
print(set2 == set1)
set2 = (1, 2, 2, 3, 3, 3, 1)
print(set2 == set2)
# A set is very useful when we need to know if the items in two iterables are the same.
# Using set() on both iterables before comparing them will remove duplicates and ignore the order.
list1 = [1, 2, 3]
list2 = [1, 1, 2, 2, 3, 3, 3]
print(set(list2) == set(list1))


