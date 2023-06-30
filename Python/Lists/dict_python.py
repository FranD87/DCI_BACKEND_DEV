# Dictionaries are associative arrays.
# They:
# Have an order.
# Allow duplicate values.
# Allow their objects to be changed.
# Allow objects of different types.

my_dict = {
    'name': 'Julia',
    'address': 'Bla bla street',
    'number': 4,
    'language': ['Russian', 'Ukraine', 'English', 'Arabic']
}
print(my_dict['number'])
print(my_dict.get('name'))
print(my_dict.get('unknown', True))  # in get method we can specify default value wat will be returned if key does not
# exists if default not specified it will give None
print(my_dict)
# dict can be created with fromkey method
template = dict.fromkeys(['Name', 'Address', 'Age'], 'Not created')  # We can specify only 1 value as default
print(template)

# we can set default value for dic and this value will be added to dic
my_dict.setdefault('Pet', 'Cat')  # Work same as get but will actually add this item to dic
print(my_dict)
# add values to dic
my_dict['fname'] = 'Shcherbyna'  # To create or change value
print(my_dict)
# Merging 2 dict
dic_to_merge = {
    'name': 'Olga',
    'age': 30,
    'country': 'Germany'
}
my_dict.update(dic_to_merge)
print(my_dict)
# remove item from the dict
print(my_dict.popitem())  # remove last, do not take params, return tuple
print(my_dict)
print(my_dict.pop('name'))  # remove exact item, return value
print(my_dict)
new_dic = my_dict.copy()
print(new_dic)
new_dic.clear()
print(new_dic)

# key, value, item methods
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

# comparing
dic1 = {1: 'a', 2: 'b', 3: 'c'}
dic2 = {1: 'a', 3: 'c', 2: 'b'}
print(dic2 == dic1)

