# Create a list
my_list = ['String', 2, True, ['A', 'B', 3], 4.789]
# We can convert to list any iterable
list_from_string = list('Hello World')
# print(list_from_string)
# Creating empty list
empty_list = list()
other_empty_list = []
# print(empty_list)
# print(other_empty_list)
# We can generate list of integers with range()
int_list = list(range(1, 10, 2))
# print(int_list)
# We can access any item in list by index
print(my_list[0])
# We can slice the list
print(my_list[1:3])
print(my_list[-2:])
print(my_list[::-1])
fruits = ['Apple', 'Banana', 'Grape', 'Orange', 'Grape']
# We can get index of some item
print(fruits.index('Apple'))
print(fruits.index('Grape'))  # In this case first index will be returned
# We can get amount of items in list
print(fruits.count('Grape'))
# We can reverse list
print(fruits[::-1])
print(fruits)  # We can see that order not changed
print(fruits.reverse())  # This will return None because by this action we reverse the string and store it
print(fruits)
# We can sort the list
fruits.sort()
print(fruits)
# Or sort it with reverse
fruits.sort(reverse=True)
print(fruits)
# We can change value of item
fruits[0] = 'Dragon Fruit'
print(fruits)
fruits[0:2] = ['Ananas']
print(fruits)
fruits[0] = None
print(fruits)
fruits[0] = []
print(fruits)
fruits.append('Apple')
berries = ['Blueberry', 'Strawberry']
fruits = fruits + berries
print(fruits)
# alternatively to + we can use extend() method
fruits.extend(berries)
print(fruits)
# We can insert to our list item in any place
fruits.insert(1, 'Papaya')
print(fruits)
# To remove item from the list use pop or remove method
# pop without parameters will remove last item and return it, so we can save it to var
last_item = fruits.pop()
print(fruits)
print(last_item)
item3 = fruits.pop(3)
print(item3)
print(fruits)
# remove method will remove first item what it finds and return None
fruits.remove('Papaya')
print(fruits)
fruits.append('Appended string')
# Comparing lists
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2)
print(list1 is list2)
list3 = list2[::-1]
print(list1 == list3)

