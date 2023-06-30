a = 'this is some string'
# slicing string
# string is just a bunch of characters each of what have index start from 0
# string[x:]
# 	Extract the last slice of  characters starting from the x index value.

# string[:y]  # Extract the first slice of characters until the y index value.

# String[x:y:stride]
# 	The new parameter stride refers to how many characters to move
# 	 forward after the first character is retrieved from	the string.
print(a[1])
print(a[5:])
print(a[5:10])
print(a[0::2])

a = 'this is some string'
# b = a.find('is')  # in this case b value is result of find() method
# print(b)

print(a.find('###'))

# b = a.index('is')  # This method is used to finds the first occurrence of the specified value and return its
# index.  This works similar to find, but it returns an exception if the value is not found, so we need to handle it
# with a catch statement.
# print(b)
# Output:
# ValueError: substring not found

c = 'this is something great # I love it'
# This method is used to split a string in a list of words. The separator defines the base String to split with
# (e.g. dash), the whitespace is default. The maxsplit refers to how many splits to do and it is optional.
print(c.split())
# Output
# ['this', 'is', 'something', 'great', '#', 'I', 'love', 'it']
print(c.split(sep='#'))


# ALL STRING METHODS RETURN NEW VALUE THEY DO NOT CHANGE ORIGINAL STRING

print(c.replace('i', '*'))
# Output:
# th*s *s someth*ng great # I love *t

c = 'Hello World'
print(id(c))
c.replace(' ', '#')
print(id(c))
print(c)
c = c.replace(' ', '#')
print(id(c))
print(c)

print(c.count('i'))  # will count characters in string
# Output:
# 4

# Strip
c = '         hello, Julia    '
print(c.strip())  # Built-in function to remove leading and trailing whitespaces
print(c.rstrip())  # rstrip removes  leading and trailing whitespaces from “right” side of string
print(c.lstrip())  # lstrip removes  leading and trailing whitespaces from “left” side of string
c = '###hello######'
print(c.strip('#'))

s = 'Patrick'.startswith('Pat')  # case sensitive!
print(s)
s = 'Patrick'.endswith('k')  # case sensitive!
print(s)

s = 'Python is awesome!'
s = s.center(30, '-')
# ------Python is awesome!------
print(s)
s = 'Python is awesome!'
s = s.ljust(30, '-')
# Python is awesome!------------
print(s)
s = 'Python is awesome!'
s = s.rjust(30, '-')
# ------------Python is awesome!
print(s)

# Return a copy of the string with uppercase characters converted to lowercase and vice versa.
s = 'HELLO world'
s = s.swapcase()
print(s)
# 'hello WORLD'

str1 = 'Hello'
str2 = 'World!'
print(str1 + ' ' + str2)

print(str1 * 3)
# Output:
# HelloHelloHello

# String format
x = 'Hello {}, your pet name is {}'.format('Julia', 'Grey')
print(x)

x = 'Hello {1}, your pet name is {0}'.format('Grey', 'Julia')  # index of passed value
print(x)

x = 'Hello {name}, your pet name is {petname}'.format(petname='Grey', name='Julia')  # example with parameter
print(x)

name = 'Julia'
petname = 'Grey'
x = f'Hello {name}, your pet name is {petname}'  # example with variables
print(x)

x = f'Hello {name.upper()}, your pet name is {petname.upper()}'
print(x)

for char in x:
    if char == 'i':
        print('This is i')

for i in range(len(x)):
    print(i)
    print(x[i])

# Interesting thing about string modification

# if you want to create string with 1 000 000 of a
# since a string is immutable, adding strings with +,  or += always
# creates a new string, and therefore is expensive for multiple operations
# --> join method is much faster
from timeit import default_timer as timer

my_list = ["a"] * 1000000
# bad
start = timer()  # here I just create timer what will start and finish and will give me amount of sec while script
# was running
a = ""
for i in my_list:
    a += i
end = timer()

print(f"concatenate string with + : {end - start}")

# good
start = timer()
b = "".join(my_list)
end = timer()
print(f"concatenate string with join(): {end - start}")
print(a == b)


# +-------------+-----------+-------------+----------------------------------+
# | isdecimal() | isdigit() | isnumeric() |          Example                 |
# +-------------+-----------+-------------+----------------------------------+
# |    True     |    True   |    True     | "038", "੦੩੮", "０３８"            |
# |  False      |    True   |    True     | "⁰³⁸", "🄀⒊⒏", "⓪③⑧"          |
# |  False      |  False    |    True     | "↉⅛⅘", "ⅠⅢⅧ", "⑩⑬㊿", "壹貳參" |
# |  False      |  False    |  False      | "abc"                            |
# +-------------+-----------+-------------+----------------------------------+
