Python Debugging
Task 1
You have been provided a function that loops over a list and returns the total of the values provided in the list

def get_total(lst):
index = 0
total = 0
while index < len(lst):
total += lst[index]
index += 1

    print(total)

    return total
Spend some time introducing the debugger using 2 approaches

First approach
Run debugger as a script

python -m pdb file_name.py

Second approach
Add a break point to your code

Steps for your experiment
Retrieve the following information

A print out of the list of arguments of the function
Navigate through the function using n
Skip the while loop statement in your breakpoint to go to the line with the print statement