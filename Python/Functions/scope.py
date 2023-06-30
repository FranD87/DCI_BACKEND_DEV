name = 'Julia'
my_list = ['Julia', 2, 2.3]
print(id(name))
print(id(my_list))

def test_func(par_name, par_list):
    par_name = 'Jon'  # We change value of string inside the function
    par_list[0] = 'Jon'  # We change value of list item inside the function
    print(id(par_name))
    print(id(par_list))
test_func(name, my_list)
print(my_list)  # List was changed as it is mutable type of data
print(name)  # String was not changed because t is immutable
    



