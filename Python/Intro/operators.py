x = 2
y = 3
# OPERATORS
# +	Addition	x + y
# -	Subtraction	x - y
# *	Multiplication	x * y
# /	Division	x / y
# %	Modulus	x % y 7%2 = 1 (rest)
# ** Exponentiation	x ** y x to the power of y
# // Floor division	x // y 7//2 = 3 (round value)

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

# BUILD IN math functions
# max() - return max value from param
# min() - return min value from param
print(max(2, 10, 18765))
print(min(2, 9, 189, 5678, 8765))
print(max('A', 'b', 'C'))

# The abs() function returns the absolute (positive) value of the specified number

print(abs(-3))
print(abs(87))

# The pow(x, y) function returns the value of x to the power of y, same as x ** y
print(pow(2, 3))
# The round() function returns a floating point number that is a rounded version of the specified number
print(round(1.23))
print(round(1.78))

# specified number of decimals.
# The default number of decimals is 0, meaning that the function without second argument will return the nearest integer
# round(1.23) -> 1
# round(1.82) -> 2
# If you want to round float to specific decimal number just pass it as parameter

print(round(1.98732768743296, 3))

# math module
# to import in file use import math
# to import in shel use >>> import math

import math

# The math.sqrt() method for example, returns the square root of a number
x = math.sqrt(49)
print(x)

# The math.ceil() method rounds a number upwards to its nearest integer, and the math.floor() method rounds a number
# downwards to its nearest integer, and returns the result
y = math.ceil(8.24)
z = math.floor(8.24)
print(y, z)

# ASSIGNMENT OPERATORS
# =	    x = 5	x = 5
# +=	x += 3	x = x + 3
# -=	x -= 3	x = x - 3
# *=	x *= 3	x = x * 3
# /=	x /= 3	x = x / 3
# %=	x %= 3	x = x % 3
# //=	x //= 3	x = x // 3
# **=	x **= 3	x = x ** 3

x = 5
y = 3
# x += y
# x -= y
# x *= y
# x /= y
# x %= y
# x **= y
# x //= y
print(x)

# Binary, Oct, Hex definition by prefix
print(0b10)
print(0o10)
print(0x10)

# Built-in function bin() converts an integer number to a binary string prefixed with “0b” (zero and b). The result is
# a valid Python expression

print(bin(13))

# Built-in function int() returns an integer object constructed from a number or string
# To convert from binary to integer we must set second argument of int() called base. For binary numbers the base is 2

print(int('1101', 2))
