import calendar

yy = 2023
mm = 11

# display the calendar
print(calendar.month(yy, mm))

# using calendar to print calendar of year
# prints calendar of 2018
print("The calendar of year 2023 is : ")
print(calendar.calendar(2023))

# check is year leap
print(calendar.isleap(2023))


calendar.setfirstweekday(2)  # we set first weekday to Wednesday
print(calendar.month(2023, 1))  # we print out calendar where first weekday is Wednesday

print(calendar.firstweekday())  # we will receive 2 as we set first weekday to Wednesday, default is 0

