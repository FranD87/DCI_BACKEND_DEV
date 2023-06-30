# Task 1
# loop dictionary with enumerate function for each item in dictionary print with formatted string method:
# Hello I am item of dictionary with key 'age' my value is '54' and my position in dictionary is 1
my_dict = {
    'name': 'Bob',
    'age': 54,
    'address': 'Bla-Bla street',
    'grade': 3,
    'city': 'Berlin',
    'country': 'Germany'
}
# Task 2
names = ['Bob', 'Marlen', 'Jessica', 'David', 'Piet']
countries = ['Germany', 'Portugal', 'USA', 'England', 'Germany']
prize = ['Car', '10 000$', 'Vacation in Maldives', 'Dinner in restaurant', 'Treap to Disneyland']
# You have list of winners and list of countries from where they are. Create a program what will randomly generate
# prize for them from list prize. Use zip function to create tuple of (name, country, prize), note each time your
# program run prizes should be generated differently. For each generated tuple print out formatted string.
# Example of output:
# Prize for Jessica from the USA is 10 000$ -> prize should be each time different

# Task 3
# Create a code for sort_profile function what will take dictionary of people profiles, sort_by parameter what will be
# integer:
#      1 -> sort by name,
#      2 -> sort by age,
#      3 -> sort by tall,
#      4 -> sort by weight
# And reverse bool optional parameter if it was passed to sort_profiles function and its value is True profiles
# should be sorted with reverse
dict1 = [
   {"name": "John", "age": 31, 'tall': 1.76, 'weight': 79},
   {"name": "Mary", "age": 46, 'tall': 1.69, 'weight': 55},
   {"name": "Lucy", "age": 25, 'tall': 1.97, 'weight': 102}
]
def sort_profiles(profiles, sort_by, reverse=False):
    '''

    :param profiles: list of dictionaries with profile of people
    :param sort_by: int if:
     1 -> sort by name,
     2 -> sort by age,
     3 -> sort by tall,
     4 -> sort by weight
    :param reverse: by default false, if true sort with reverse
    :return: sorted dictionary
    '''
    # Write your code here
    pass
# Example:
# sort_profiles(dict1, 4, reverse=True)
# Output:
# [
#    {"name": "Lucy", "age": 25, 'tall': 1.97, 'weight': 102},
#    {"name": "John", "age": 31, 'tall': 1.76, 'weight': 79},
#    {"name": "Mary", "age": 46, 'tall': 1.69, 'weight': 55},
#
# ]

# Task 4
# Write a code to insert a string 'emp' at the beginning of all items in a list. Use map() function for implementation
# Sample list : [1, 2, 3, 4, 5]
# Expected output : ['emp1', 'emp2', 'emp3', 'emp4', 'emp5']
# NOTE: Items in given string can be str, int, float NOT list, tuple, set or dictionary

# Task 5
# Write a program with filter() function what will filter all pdf file names from list
files_list = ['image3464456.jmp', 'class.pdf', 'requirenments.txt', 'some_data.md', 'presentation.pdf', 'my presentation.pdf', 'dog.jpeg']




