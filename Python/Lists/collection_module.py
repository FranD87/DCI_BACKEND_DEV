# Counting how many occurrences of the same value are found in an iterable requires at least 5 lines of code.
fridge = ['Apple', 'Apple', 'Cabbage', 'Steak', 'Cheese', 'Apple', 'Carrot', 'Carrot', 'Yogurt', 'Beer']
counter = {}
for ingredient in fridge:
    if ingredient not in counter:
        counter[ingredient] = 0
    counter[ingredient] += 1
from collections import Counter
counter = Counter(fridge)
print(counter)
# The method total will return the sum of all the occurrences, which should be the length of the iterable passed to
# the Counter constructor.
print(counter.total())
# The method subtract will subtract a counter from another counter.
# This will modify the original counter and will return None.
# The minus operator - can also be used to obtain a similar result but returning a new counter, and not changing the
# original counter.
lunch = Counter(Cabbage=1, Carrot=1)
counter.subtract(lunch)
print(counter)
# The method update will add a counter to another counter.
# This will modify the original counter and will return None.
# The plus operator + can also be used to obtain a similar result but returning a new counter, and not changing the
# original counter.
shopping = Counter(Carrot=10, Beer=7, Cabbage=3, Cream=5)
counter.update(shopping)
print(counter)
print(id(counter))
counter = counter + shopping
print(id(counter))
print(counter)
# The method most_common will return a list sorted by occurrence in descending order that can be iterated in the
# same order.
# The items of the list will be tuples containing both the value and the counter of each item.
# This method accepts a positional argument to limit the amount of items returned (i.e: get the n most repeated items).
print(counter.most_common())
common_5 = counter.most_common(5)
print(common_5)
for item in counter.most_common():
    print(item)
# The method clear will empty the counter and remove all the items.
counter.clear()
print(counter)
counter1 = Counter(Apple=3, Banana=2)
counter2 = Counter(Banana=1, Cabbage=8)
print(counter2 + counter1)
print(counter1 - counter2)
print(counter2 & counter1)  # will return item and amount what exist in both counters
print(counter2 | counter1)  # return items from 1 and from 2, for items what exist in both will return bigger
print(counter2 == counter1)

from collections import OrderedDict
my_dict = {
    'name': 'Bob',
    'age': 54,
    'country': 'Germany'
}
my_ordered_dict = OrderedDict(my_dict)
print(type(my_ordered_dict))
print(my_ordered_dict)  # Basically this was implemented by storing tuple of key/value in list
my_ordered_dict.move_to_end('name')
print(my_ordered_dict)
my_ordered_dict.move_to_end('name', last=False) # last=False will move to beginning
print(my_ordered_dict)
# The ChainMap type is very similar to the update method in dictionaries.
# It merges together a series of dictionaries, but instead of updating one of them it just returns a new object.
# Items are merged from right to left.
# The ChainMap object is a dictionary-like object and its items can be accessed using the keys.
from collections import ChainMap
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict1 = {'d': 4, 'e': 5, 'f': 6}
chain = ChainMap(my_dict, my_dict1)
print(chain)
print(dict(chain))
print(chain['a'])
# The ChainMap is more than just a method of updating dictionaries, it has memory. It remembers which dictionaries
# were merged to produce the object.
# It has a property maps, as a list of input elements. This list can be manipulated and the main object will be changed.
print(chain.maps)
chain.maps[0]['b'] = 100
print(chain)
# A ChainMap is a dictionary-like object and can also be used as an argument of another ChainMap.
# This is used often to provide configuration objects that can work in different contexts. Each ChainMap in the tree
# represents a context that inherits from another parent or default context.
my_dict3 = {'d': 7, 'h': 8, 'i': 9}
chain1 = ChainMap(my_dict3, chain)
print(chain1)
print(chain1.maps[0])
print(chain1.maps[1])
print(chain1['d'])
print(chain1.maps[1]['d'])
# A namedtuple creates a new custom data type with the name and attributes indicated.
# It requires a string for the name of the type and a list of attributes.
# Creating new objects of that type can be done by using the constructor and passing the data as positional arguments.
from collections import namedtuple
MyAddress = namedtuple('Address', ['street', 'number', 'city', 'county'])
home = MyAddress('Bla-Bla street', 13, 'Lueburg', 'Germany')
print(home)
# The elements in a namedtuple have an implicit order and can be accessed using indices.
# They can also be accessed using dot notation. This often provides a more readable code.
# It is often used when dealing with CSV files and other tabular read-only data.
print(home[2])
print(home.city)
# home[0] = "Somewhere else"
# TypeError: 'Address' object does not support item assignment
# home.street = "Somewhere else"
# AttributeError: can't set attribute
# home = MyAddress("Private Drive", 4)
# TypeError: <lambda>() missing 2 required positional arguments: 'city' and 'county'

# A namedtuple has some useful methods.
# The _asdict method will return a dictionary with the data.
# The _replace method will return a new object with the new values given.
# The original object is still read-only and does not change.
print(home._asdict())
new_home = home._replace(number=6)
print(id(new_home))
print(id(home))




