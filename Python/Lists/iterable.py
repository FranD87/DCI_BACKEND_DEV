my_list = ['Maria', 'Bob', 'Micael', 'David']
for item in my_list:
    print(item)
for i in range(len(my_list)):
    print(i)
    print(my_list[i])

my_dict = {
    'name': 'Bob',
    'age': 15,
    'country': 'Germany'
}

for item in my_dict:
    print(item)
    print(my_dict[item])

for key in my_dict.keys():
    print(key)
    print(my_dict[key])

for value in my_dict.values():
    print(value)

for key, value in my_dict.items():
    print(key, '->', value)

# Another common pattern is to use tuples instead of dictionaries to store key-value pairs that need to remain
# constant. This can be done defining a bi-dimensional tuple (a tuple of tuples).
# The iteration will yield a tuple that can be unpacked like we do with the items method of a dictionary.
days = (
    ('Mon', 'Monday'),
    ('Tue', 'Tuesday'),
    ('Wed', 'Wednesday'),
    ('Thu', 'Thursday'),
    ('Fri', 'Friday'),
    ('Sat', 'Saturday'),
    ('Sun', 'Sunday')
)
for key, value in days:
    print(key, '=>', value)

# Enumerate function add a counter to iterable
days_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
for index, value in enumerate(days_list):
    print(index, '=>', value)
# This is the same as:
# position = 0
# for value in list:
#   print(position, "=>", value)
#   position += 1

my_dict = {
    'name': 'Mary Schmidt',
    'age': 54
}
for position, value in enumerate(my_dict.items()):
    print(position, '=>', value)

for position, (key, value) in enumerate(my_dict.items()):
    print(position, '.', key, '=>', value)

# zip function
numbers = [1, 2, 3, 4]  # 4 will not be zipped
names = ('One', 'Two', 'Three')
zip1 = zip(numbers, names)
for item in zip1:
    print(item)

nums = "123"
eng = ("one", "two", "three")
cat = {"un": 1, "dos": 2, "tres": 3}
fra = ["un", "deux", "trois"]
for item in zip(nums, eng, cat, fra):
    print(item)
# What will happen if we will add set?
deu = {"ein", "zwei", "drei"}
for item in zip(nums, eng, cat, fra, deu):
    print(item)
# max min sum functions for iterable
nums = [1, 2, 3, 4, 5]
print(max(nums))
print(min(nums))
print(sum(nums))
# What will happen if inside iterable will be string?
# nums = {1, 2, 3, 4, '5'}
# can we implement this function with strings?
nums = ["a", "b", "c", "d", "e"]
print(max(nums))
print(min(nums))
# how it processed?

# The sorted function returns a new list in alphabetical or numerical order.
nums = [4, 3, 5, 2, 1]
sorted_nums = sorted(nums)
print(sorted_nums)
dict1 = {"c": 2, "b": 1, "a": 3}
sorted_dict = sorted(dict1)
# Sorting a dictionary with sorted will return a list with the keys in alphabetical order, because the default
# iterable of a dictionary is by key.
print(sorted_dict)
# Getting the sorted list of values can be done using the values method.
print(sorted(dict1.values()))
# It accepts a keyword argument named reverse as a boolean that defaults to False.
print(sorted(dict1, reverse=True))

# sort list of dict
# The sorted function can also be used on lists of dictionaries to sort the list based on the values of one of the
# keys in these dictionaries.

# The sorted function can also be used on lists of dictionaries to sort the list based on the values of one of the
# keys in these dictionaries.
dict1 = [
   {"name": "John", "age": 31},
   {"name": "Mary", "age": 46},
   {"name": "Lucy", "age": 25}
]
by_age = lambda user: user["age"]
by_name = lambda user: user["name"]
# This can be done passing a function as the key argument. This function should return the value to be used for sorting.
print(sorted(dict1, key=by_age))
print(sorted(dict1, key=by_name))

# Some functions use iterables to return a boolean value indicating if the iterable matches a certain condition.
# The function any will return True only if any of the values in the iterable is truthy.
# The function all will return True only if all the values in the iterable are truthy.
a_list = [1, True, "Mary", {1, 2}]
print(any(a_list), all(a_list))
a_list = [1, True, "Mary", {}]
print(any(a_list), all(a_list))
a_list = [0, False, "", {}]
print(any(a_list), all(a_list))

# The most common functions in functional programming require both an iterable and a function.
# This is the case of the map function, that applies the given function to each element of the given iterable.
# It returns a map object that is an iterable containing the output of that process.
a_list = [1, 2, 3, 4, 5]
by_two = lambda num: num * 2
a_list_by_two = map(by_two, a_list)
print(a_list_by_two)
print(list(a_list_by_two))

# The filter function returns an iterable with the elements of the given iterable that match a condition defined in
# a function.
# It returns a filter object that is an iterable containing the output of that process.
is_odd = lambda num: (num % 2) != 0
odds = filter(is_odd, nums)
print(odds)
print(list(odds))



