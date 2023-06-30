# and	Logical AND: True if both the operands are true	x and y
# or	Logical OR: True if either of the operands is true	x or y
# not	Logical NOT: True if operand is false	not x

# or example
result = input('Are you a human? Y/y\n')
if result == 'Y' or result == 'y':
    print('this is human')
else:
    print('This is not human')

# and example
number = int(input('Please enter the number\n'))
if number > 0 and number < 100:
    print('This is number from 1 to 99')
else:
    print('This is number less than 1 or bigger than 99')

# not example
number = int(input('Please enter the number\n'))
if not(number > 0 and number < 100):
    print('This is number less than 1 or bigger than 99')
else:
    print('This is number from 1 to 99')

# if else statement in one line
a = 3
b = 5
print("A") if a > b else print("B")  # this is simplified syntax for if/else statement

# is and is not operator
# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object,
# with the same memory location


i = 1987
j = 1987
print(id(i))
print(id(j))
print(i is j)

a = [1, 3, 4]
b = [1, 3, 4]

print(id(a))
print(id(b))
print(a is b)

# Only None, True and False have guaranteed same ID in Python


# in and not in operators
# Membership operators are used to test if a sequence is presented in an object
a = 'Julia'

print('J' in a)
print('J' not in a)



