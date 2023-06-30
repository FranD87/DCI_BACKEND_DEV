#Write a program that carries out the four basic mathematical operations.
#Your program should take any two numbers and an operation from the user and then carry out the operation.
from calculator import Calculator, Mathematics

x = int(input('Please enter the first number: '))
y = int(input('Please enter the second number: '))
oper = input('Please enter the operation: ')
val = -51
#cal = Calculator(x, y, oper)

cal = Mathematics(x, y, oper, val)

if oper=='+':
    print(cal.addition())
elif oper=='-':
    print(cal.subtraction())
elif oper=='*' or oper=='x':
    print(cal.multiplication())
elif oper=='/':
    print(cal.division())

print(f'Absolute value of {val} is {cal.absolute()}')
print(f'Square value of {val} is {cal.square()}')
print(f'Mod value of {x} and {y} is {cal.modulus()}')
#print(f'The value is {cal.setValue(val)}')
print(f'The value is {cal.getValue()}')