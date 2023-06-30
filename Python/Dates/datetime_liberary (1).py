import datetime

# This method is used to get the current local date and time of the day.
print(datetime.datetime.today())

# This method is used to get the current local date (without the time)
print(datetime.date.today())


# Create a datetime instance by providing keyword arguments such as year, month, day, hour minute and second.
print(datetime.date(year=1986, month=6, day=13))

# See the list of methods you have access to
# print(dir(datetime))



# ISO 8601 is an internationally agreed way to represent dates. (YYYY-MM-DD). ISO 8601 can be used by anyone who wants
# to use a standardized way of presenting datetime, UTC, and local time with offset to UTC.

# In Python ISO 8601 date is represented in YYYY-MM-DD HH:MM:SS.mmmmmm format. For example, May 18, 2022, is
# represented as 2022-05-18 11:40:22.519222.
#
# Here:
#
# YYYY: Year in four-digit format
# MM: Months from 1-12
# DD: Days from 1 to 31
# T: It is the separator character that is to be printed between the date and time fields. It is an optional parameter
# having a default value of “T”.
# HH: For the value of hours
# MM: For the specified value of minutes
# SS: For the specified value of seconds
# mmmmmm: For the specified microseconds

# Creates a datetime object using date represented as an ISO 8601 String.
print(datetime.date.fromisoformat('2018-01-31'))


# to create date with time
test_date = datetime.datetime(year=2022, month=2, day=14, hour=18, minute=31, second=54, microsecond=18)
# microseconds 6 digits
print(test_date)

# Format Datetime:

# Directive	Description	Example
# %a	Weekday, short version	Wed
# %A	Weekday, full version	Wednesday
# %w	Weekday as a number 0-6, 0 is Sunday	3
# %d	Day of month 01-31	31
# %b	Month name, short version	Dec
# %B	Month name, full version	December
# %m	Month as a number 01-12	12
# %y	Year, short version, without century	18
# %Y	Year, full version	2018
# %H	Hour 00-23	17
# %I	Hour 00-12	05
# %p	AM/PM	PM
# %M	Minute 00-59	41
# %S	Second 00-59	08
# %f	Microsecond 000000-999999	548513
# %z	UTC offset	+0100
# %Z	Timezone	CST
# %j	Day number of year 001-366	365
# %U	Week number of year, Sunday as the first day of week, 00-53	52
# %W	Week number of year, Monday as the first day of week, 00-53	52
# %c	Local version of date and time	Mon Dec 31 17:41:00 2018
# %C	Century	20
# %x	Local version of date	12/31/18
# %X	Local version of time	17:41:00
# %%	A % character	%
# %G	ISO 8601 year	2018
# %u	ISO 8601 weekday (1-7)	1
# %V	ISO 8601 weeknumber (01-53)	01

# Example
print(test_date.strftime('%A, %d %B %Y %H:%M %p'))

# Timedelta
delta = datetime.timedelta(days=365)  # Creating timedelta
new_date = test_date + delta  # adding timedelta to our date
print(new_date.strftime('%A, %d %B %Y %H:%M %p'))  # Printing created new_date in user friendly format

