# Print "Weekend" if the day is Saturday or Sunday; otherwise, print "Weekday".

import datetime
from zoneinfo import ZoneInfo

list_weekday = { 1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thrusday', 5:'Friday'}

list_weekend = { 6:'Saturday', 7:'Sunday'}

hyderabad_tz = ZoneInfo("Asia/Kolkata")

# Get the current datetime in Hyderabad
current_datetime_hyd = datetime.datetime.now(tz=hyderabad_tz)

# Extract only the time component
current_day = current_datetime_hyd.isoweekday()


if current_day in list_weekend:
    print(f'This is a weekend as today is {list_weekend[current_day]}')
else:
    print(f'This is a weekday as today is {list_weekend[current_day]}')

#print(current_day)

#on_time = datetime.time(12, 0, 0) # hour=12, minute=0, second=0


'''
output
--------
This is a weekend as today is Sunday
'''