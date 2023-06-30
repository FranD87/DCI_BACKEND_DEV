my_iterable = iter('Hello')
print(my_iterable)
my_iterable1 = iter(range(23))
print(my_iterable1)
print(next(my_iterable))
print(next(my_iterable))
# for i in range(4):
#     print(next(my_iterable))  # will give error
# You can create 2 iterators in same object
itr1 = iter('Hello')
itr2 = iter('Hello')
print(next(itr1))
print(next(itr1))
print(next(itr2))
# to grab all values from iterator at once use list()
print(list(itr2))

for i in range(4):
    print(i)
else:
    print('End of iterating')

n = 5
while n > 0:
    n -= 1
    print(n)
else:
    print('End')
while n > 0: n -= 1; print(n)  # example of while in line
for i in 'Hello': print(i)
# The continue keyword is used to end the current iteration in a for loop (or a while loop), and continues to the
# next iteration
for i in range(10):
    if i == 5 or i == 8:
        continue  # Skip the iteration if the variable i is 5 or 8, but continue with the next iteration.
    else:
        print(i)
# The break keyword is used to break out a for loop, or a while loop.
i = 0
while i < 10:
    i += 1
    print(i)
    if i == 5:  # With the break statement we can stop the loop even if the while condition is true
        break


