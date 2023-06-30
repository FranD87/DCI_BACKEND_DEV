import time

# In the above example, we have used the time.time() function to get the current time in seconds since the epoch, and
# then printed the result.
print(time.time())  # we get current time in seconds

# The time.ctime() function in Python takes seconds passed since epoch as an argument and returns a string
# representing local time.
print(time.ctime(1673256581.6581137))

print('print it out now')
# The sleep() function suspends (delays) execution of the current thread for the given number of seconds.
time.sleep(2.4)
print('This will be printed out with delay')

# The localtime() function takes the number of seconds passed since epoch as an argument and returns struct_time
# (a tuple containing 9 elements corresponding to struct_time) in local time.
seconds = 1673256581.6581137
result = time.localtime(seconds)
print(result)  
print(result.tm_year)


# The gmtime() function takes the number of seconds passed since epoch as an argument and returns struct_time in UTC.
gm_time = time.gmtime(seconds)  # this will print out time in UTC
print(gm_time)
print(gm_time.tm_sec)

# The strftime() function takes struct_time (or tuple corresponding to it) as an argument and returns a string
# representing it based on the format code used.
my_time = time.localtime()
result = time.strftime('%d %Y %m %H%M%S', my_time)
print(result)
print(time.strftime('DATE:%A %y %B TIME:%I:%M:%S %p', my_time))
# all list of special characters to format time see here:
# https://docs.python.org/3/library/time.html#time.strftime

# The strptime() function parses a string representing time and returns struct_time.
string_time = '13 January 2021'
result = time.strptime(string_time, '%d %B %Y')  # here it is important to know what string you will get
print(result)

