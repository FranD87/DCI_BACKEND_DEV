
c = 'this "is" string'
d = "This 'is' also string"
print('Hello', sep='#', end='!')
e = False
f = None  # This is None Type
'''
This is multi line comment
'''
"""
This is also multiline comment
"""
print(type(c))
g = int('3')
h = float('3.75')
i = str(10)
print(type(g), type(h), type(i))
print(id(g))  # this will give us exact id of stored value

print(bool(0), bool(1), bool(''), bool('not empty string'), bool(None))  # some default values of bool

j = max(4, 108, 0, 276)
k = min(2, 987, -654, 0)
l = abs(-987)
m = round(2.85668743562383465, 2)  # without 2 parameter it will round math way, with 2 param it will round till
# specified digits

print(j, k, l, m)

from math import sqrt, floor  # import math -> import math as m
n = sqrt(121)
o = floor(2.786)
print(n, o)

p = 7
q = 3

print(p + q)  # Addition
print(p - q)  # Subtraction
print(p * q)  # Multiplication
print(p / q)  # Division
print(p % q)  # Rest
print(p // q)  # Round value after Division
print(p ** q)  # Power

p += 2  # -> p = p + 2
p -= 2  # -> p = p - 2
p *= 2  # -> p = p * 2
p /= 2  # -> p = p / 2
p %= 2  # -> p = p % 2
p **= 2  # -> p = p ** 2
p //= 2  # -> p = p // 2

r = input('Enter number\n')  # Result will be always string
if int(r) < 0:
    print('This is negative number')
elif 0 < int(r):
    print('This is positive number')
else:
    print('This is 0')

if int(r) == 0: print('this is 0')  # Different syntax for single if statement

category = input('please enter your category A -> Admin/ U -> User')
if int(r) < 0:
    if category == 'A':
        print('Hello Admin, this is negative number')
    elif category == 'U':
        print('Hello User, this is negative number')
    else:
        print('Your category was not defined, this is negative number')
elif int(r) > 0:
    if category == 'A':
        print('Hello Admin, this is positive number')
    elif category == 'U':
        print('Hello User, this is positive number')
    else:
        print('Your category was not defined, this is positive number')
else:
    if category == 'A':
        print('Hello Admin, this is 0')
    elif category == 'U':
        print('Hello User, this is 0')
    else:
        print('Your category was not defined, this is 0')

# Compression Operators
# ==	Equal	                    x == y
# !=	Not equal	                x != y
# >	    Greater than	            x > y
# <	    Less than	                x < y
# >=	Greater than or equal to	x >= y
# <=	Less than or equal to	    x <= y

x = 4
y = 10
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# REPETITION STATEMENTS

# FOR LOOPS
str_var = 'Julia'

for i in str_var:
    print(i)

# To loop through a set of code a specified number of times, we can use the range() function
for i in range(5):
    print(i)

# It is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6
# (but not including 6)

for i in range(3, 9):
    print(i)

# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value
# by adding a third parameter

for i in range(3, 9, 2):
    print(i)

# The else keyword in a for loop specifies a block of code to be executed when the loop is finished

for i in range(4):
    print(i)
else:
    print('Finally finished')

# WHILE LOOP
i = 1
while i < 5:
    print(i)
    i += 1


# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to
# avoid getting an error
for i in range(9):
    pass


