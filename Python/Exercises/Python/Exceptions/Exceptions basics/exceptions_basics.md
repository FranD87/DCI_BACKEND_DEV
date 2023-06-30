Python basics - Exceptions-II
IIa: Theoretical Warm Up
Write short answers (2-5 sentences) to the following questions:

Name three things that exception processing is good for.
What happens to an exception if you don’t do anything special to handle it?
How can your script recover (program continuation) from an exception?
What is the try statement for?
What are the two common variations of the try statement?
What is the raise statement for?
IIb: Practical Warm Up (30 mins)
Place result="You can't divide by 0" in the correct place below such that the program avoids a ZeroDivisionError.
#Type your answer below (pick the correct line).

a=5
b=0
try:
result=a/b
except ZeroDivisionError:


print(result)
Place msg="You can't add int to string" in the correct place below such that the program avoids a BaseExceptionError.
You can use except Exception, although normally you should be careful using such powerful exception statements.

#Type your answer below.

a="Hello World!"
try:
a + 10



print(msg)
Place msg="You're out of list range" in the correct place below such that the program avoids an IndexError.
#Type your answer below.

lst=[5, 10, 20]

try:
print(lst[5])



print(msg)