def hello(my_str):
    if my_str == '':  # Base case, case what will stop recursion (in our case when string will be empty)
        pass  
    else:
        my_str = my_str[1:] # we cut string so in each running of our function it will have different value
        print(my_str)
        hello(my_str)

hello('Julia')

