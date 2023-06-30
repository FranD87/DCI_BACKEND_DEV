# Command prompt can be characterized by the following elements:
# A command or program
# Zero or more command line arguments
# An output representing the result of the command
# Textual documentation referred to as usage or help
# Not every command line interface may provide all these elements

# The arguments that are given after the name of the program in the command line shell of the operating system are
# known as Command Line Arguments. Python provides various ways of dealing with these types of arguments. The three
# most common are:
# sys.argv
# getopt module
# argparse module

# The sys module in Python provides various functions and variables that are used to manipulate different parts of the
# Python runtime environment. It allows operating on the interpreter as it provides access to the variables and
# functions that interact strongly with the interpreter

# In this example, the Python interpreter takes option -c for command, which says to execute the Python command line
# arguments following the option -c as a Python program
#
#  python -c "print('Hello World')"

import sys

print(sys.argv)
file_name = sys.argv[0]  # Here would be file name
other_data = sys.argv[1:]  # here would be all other parameters what we send from Terminal

# Checking if -h or --help was sent by user
if '--help' in other_data or '-h' in other_data:
    print('-h or --help for help\n-a or --activate to activate incognito')
# Checking if -a or --activate was sent by user
elif '-a' in other_data or '--activate' in other_data:
    print('Incognito was activated')
# if all previous conditions was false run massage for program usage
else:
    print('Usage:\npython <file name> <arguments>\n-h or --help for help')
