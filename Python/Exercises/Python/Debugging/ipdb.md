Python Debugging - ipdb
Task 2
Make sure you have ipdb installed as follows

pip install ipdb
Below you have a fizz buz application that is buggy - fix it but before you do, try to use ipdb to investigate

def fizzbuzz(maximum_value):
for n in range(maximum_value):
if n % 3 == 0:
print('Fizz')
elif n % 5 == 0:
print('Buzz')
elif n % 5 == 0 and n % 3 == 0:
print('FizzBuzz')
else:
print(n)
Recap
What is the fizzbuzz algorithm?

It is a function that prints out "Fizz" when a number is a multiple of 3, prints out "Buzz" when a number is a mutliple of 5, if the number is a multiple of both 3 and 5, "FizzBuzz" gets printed, otherwise you can optionally print the value of the number (usually we loop over a range of numbers when answering this question)

Steps for your experiment
Use import ipdb; ipdb.set_trace() to help determine what could be wrong about this function
Task 3
Find the n'th number in the fibonacci sequence
The Fibonaccic sequence is defined as follows. The first number of the sequence is 0, the second number of the sequence is 1 and the following numbers in the sequence (n) are the sum of the previous 2 numbers before it.

The following function is provided as starter code for exploring

Print out the values being memoized in a set
# This function returns values quite fast O(n) time or O(n) space, it also has an error
def get_n(n, memoize={1: 0, 2: 1}):
if n in memoize:
memoize[n]
else:
memoize[n] = get_n(n - 1, memoize) + get_n(n-2, memoize)
return memoize[n]