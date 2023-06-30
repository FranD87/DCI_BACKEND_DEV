Timezones
Working with timezones
In this exercise, we will focus on working across nations and boundaries when sending products (packages) or booking meetings with our friends and clients.

Convert your birthdate in German local Time to the time in New Zealand (Auckland)
Coordinate with your Team based in Ireland, San Francisco (USA), Berlin (Germany) and Johannesburg (South Africa). You will be having a meeting with another Team at 13:35 (Moscow Time). Print out the respective times your colleagues will be meeting
Usage
datetime, dateutil should be used in the following way

from datetime import datetime
from datetuil import tz
from datetutil.relativedelta import *
Tasks
Task 1
Use your birthday or a friend's
Hint: use tz.gettz() method to setup the timezone.

birthday = datetime(..., tzinfo=...)
...

birthday_in_newzealand = birthday.astimezone(...)
Task 2
Your team is a multinational one meeting a regional leader based in Moscow, Russia, with the following regions:

Dublin / Ireland
San Francisco / USA
Berlin / Germany
Johannesburg / South Africa
Write a Python script that will print out the different times the teams will meet.

Your result should look like this, if meeting day is is 8/07/2021 at 13:35 Moscow time:
Irish participants will meet at: 11:35:00+01:00
German participants will meet at: 2021-08-01 12:35:00+02:00
South African participants will meet at: 2021-08-01 12:35:00+02:00
American participants will meet at: 2021-08-01 03:35:00-07:00
Task 3
Write a Python program to convert a UNIX timestamp like 1626430738 to a readable date

07/16/2021, 12:18:58