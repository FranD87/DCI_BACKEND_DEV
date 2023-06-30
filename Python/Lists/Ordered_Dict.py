from collections import Counter, OrderedDict, ChainMap
fridge = ['Apple', 'Apple', 'Cabbage', 'Steak', 'Cheese', 'Apple', 'Carrot', 'Carrot', 'Yogurt', 'Beer']
# print(len(fridge))
my_count = Counter(fridge)
# print(my_count)
lunch = Counter(Apple=2, Steak=1)
my_count.subtract(lunch)
# print(my_count)
shopping = Counter(Flowers=3, Banana=5)
my_count.update(shopping)
# print(my_count)
count1 = Counter(Apple=3, Banana=2)
count2 = Counter(Banana=1, Cheese=3)
print(count1 + count2)
print(count1 - count2)
print(count1 & count2)  # and
print(count1 | count2)  # or
print(count1 == count2)
print(count1 != count2)
my_dict = {
    'name': 'Bob',
    'age': 56,
    'country': 'Germany'
}
my_ordered_dict = OrderedDict(my_dict)
print(my_ordered_dict['name'])
my_ordered_dict.move_to_end('age')
print(my_ordered_dict)
my_ordered_dict.move_to_end('age', last=False)
print(my_ordered_dict)
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'d': 4, 'e': 5, 'f': 6, 'a': 3}
chain = ChainMap(dict1, dict2)
print(chain)
print(dict(chain))
dict1.update(dict2)
print(dict1)