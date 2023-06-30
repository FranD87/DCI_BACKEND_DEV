# TASK 1
# TODO create different decorators what will add html tags to string from hello() function
def make_bold(fn):
    # add <b>...</b> tag
    pass

def make_italic(fn):
    # add <i>...</i> tag
    pass

def make_underline(fn):
    # add <u>...</u> tag
    pass

@make_bold
@make_italic
@make_underline
def hello():
    return "hello world"
# print(hello())
# Output: <b><i><u>hello world</u></i></b>

@make_bold
@make_italic
def hello():
    return "hello world"
# print(hello())
# Output: <b><i>hello world</i></b>

@make_bold
@make_underline
def hello():
    return "hello world"
# print(hello())
# Output: <b><u>hello world</u></b>

# TASK 2
# TODO wrap text in normal() function with decorator
# call function:
# normal()

# run script:
# python3 simple_decorator.py

# Example of output:
# ********************
# Hello Python
# ********************

def decorator_func(func):
    pass

@decorator_func
def normal():
    print('Hello Python')

# TASK 3
# TODO explain code above, why result of calling num and num1 is different?
def decor1(func):
    def inner():
        x = func()
        return x * x
    return inner


def decor(func):
    def inner():
        x = func()
        return 2 * x
    return inner


@decor1
@decor
def num():
    return 10


@decor
@decor1
def num2():
    return 10
print(num())
print(num2())

# TASK 4
# TODO Create a Python decorator that calculates the time it takes for a function to execute and prints it to the
#  console. The decorator should take in a function as an argument, and return a new function that calls the original
#  function and prints the execution time.

# Output example:
# Execution time: 0.0107 seconds.

def calculate_time(func):
    pass

@calculate_time
def example_function():
    for i in range(1000000):
        pass

# example_function() -> call your function after you will finish








