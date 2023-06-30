my_var = lambda x, y: x + y  

def my_ldef(x):
    return x + 1
    

# print(my_var(10, 3))

def my_printer(text):
    return lambda any: f'{text}, {any}'

result = my_printer('Hello')  # lambda x: f'Hello, {x}'
print(result('Julia'))


