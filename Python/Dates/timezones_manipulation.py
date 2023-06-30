from dateutil import tz  # import module for time zones
from datetime import datetime  # import datetime library

aus_time = tz.gettz('Australia/Melbourne')  # get timezone (as string) and store it in variable
now = datetime.now()  # create datetime object in out local time
# print(now)
now_in_austr = now.astimezone(aus_time)  # change our datetime object to australian time
# print(now_in_austr)

sec_date = datetime(year=2022, month=9, day=23, hour=19, minute=21, tzinfo=tz.gettz('America/Los_Angeles'))
# we create specific datetime object and specify timezone for it in tzinfo parameter
print(sec_date)
# print(sec_date.tzname())
ber_time = tz.gettz('Europe/Berlin')  # create variable what store Berlin timezone
converted_to_ber = sec_date.astimezone(ber_time)  # convert datetime object to specific timezone
print(converted_to_ber)



