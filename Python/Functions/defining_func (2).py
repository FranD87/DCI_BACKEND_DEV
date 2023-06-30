

def simple_def(a, b):
    print('Here is simple func')
    return a + b

def other_simp_func(func, args):  
    print('Here is main func')
    return func(*args)  # we call function what we pass in params with arguments

result = other_simp_func(simple_def, [2, 3])  # we pass function as param to other function
# print(result)


def my_print(text):
    def printer():  # we create function inside main function
        print(text)
    return printer  # we return function

result = my_print('Some string to print out')  # Here result store function printer with string 'Some string to print out'
result()  # Here we run printer function with str what we pass in line 20







