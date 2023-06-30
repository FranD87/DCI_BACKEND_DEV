# 1. Explain the result
# True, True, True creates a tuple which are true.
#  first True is the value of q1, the second True is the first element of the tuple (True, True, True),
#  and the last False is the result of the comparison True == (True, True, True).

q1 = True, True, True == (True, True, True)
print(f'{q1=}')  # -> True True False
print(f'\n{"=" * 10}\n')

# 2. Explain the result

#False == False, which is True. the value of q2 is True. The first print
#statement outputs q2=True. The second print statement simply adds a line break for
# formatting.

q2 = False == False in [False]
print(f'{q2=}')  # True
print(f'\n{"=" * 10}\n')

# 3. Create the list with the values sorted by absolute number

q3_input = [32, -5, 1, -15, 41]
q3_output = sorted(q3_input, key=abs)
print(f'{q3_input=}')
print(f'{q3_output=}')
print(f'\n{"=" * 10}\n')

# 4. Round the decimal value to 2 numbers

from decimal import Decimal

q4_input = '45.98601830'
q = Decimal(q4_input)
q4_output = round(q, 2)
print(f'{q4_input=}')
print(f'{q4_output=}')
print(f'\n{"=" * 10}\n')

# 5. Search the dict for the given term in the values and return a list of corresponding keys

q5_input = {
    '1': '1 is the loneliest number.',
    '2': '2 is the first magic number in physics.',
    '3': '3 is the cost in cents to make a $1 bill in the United States.',
    '4': '4 is the number of strings on a violin, a viola, a cello, double bass, a cuatro and a ukulele, and the number of string pairs on a mandolin.',
    '5': '5 is times Muslims pray to Allah a day.',
    '6': '6 is the jersey number worn by the starting stand-off half/five-eighth in most rugby league competitions.',
    '7': '7 is the number of seconds it takes "Superman: Escape from Krypton" roller coaster to go from 0 to 100 miles per hour.',
    '8': '8 is the number of furlongs in a mile.',
    '9': "9 is the number of circles of Hell in Dante's Divine Comedy.",
    '10': '10 is the average thickness of the Arctic ice sheet in feet.',
}
q5_term = 'krypton'
q5_output = []
for key, value in q5_input.items():
    if q5_term in value.lower():
        q5_output.append(key)
print(f'{q5_output=}')
print(f'\n{"=" * 10}\n')

# 6. Code in python solution to the following: Given an array of integers, return indices of the two numbers such that
# they add up to a specific target. You may assume that each input would have exactly one solution, and you may not
# use the same element twice.

data = [1, 2, 3, 7]
target = 5
print(f'data={data}')
result = []
for i in range(len(data)):
    for j in range(i+1, len(data)):
        if data[i] + data[j] == target:
            result = [i, j]
            break
    if result:
        break
print(result)
print(f'\n{"=" * 10}\n')

# 7. Implement the factorial function in three different ways

from functools import reduce


def fact1(n: int) -> int:
    '''Implements a factorial with reduce function'''
    # write the code here
    #Have no idea!!!


print(f'{fact1(5)=}')


def fact2(n: int) -> int:
    '''Implements a factorial with recursion'''
    # write the code here
    if n == 0:
        return 1
    else:
        return n * fact2(n-1)


print(f'{fact2(5)=}')


def fact3(n: int) -> int:
    '''Implements a factorial with loop'''
    # write the code here
    result = 1
    for i in range(2, n+1):
        result = result * i
        return result if n > 1 else 1


print(f'{fact3(5)=}')
print(f'\n{"=" * 10}\n')

# 8. Find all task codes in the text with using regular expression

import re

q8_input = '''Working on QA-456 task.
Trying to finish soon. Then will continue
with GH-12.'''
q8_output = None  # NO CLUE
print(f'{q8_output=}')
print(f'\n{"=" * 10}\n')


# 9. Write a function produce a Star triangle

def star_triangle(r: int):
    # write the code here
    for i in range(1, r+1):
        print("*" * i)
star_triangle(7)
print(f'\n{"=" * 10}\n')


# 10. Write a function to check if a sequence you input is a Palindrome

def check_palindrome(s: str) -> bool:
    # write the code here
    pass


q10_output = check_palindrome("Was it a car or a cat I saw")

print(f'{q10_output=}')
