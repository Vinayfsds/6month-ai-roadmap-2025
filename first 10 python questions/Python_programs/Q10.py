#0. Print "Good Morning" if the time is before 12 PM, otherwise print "Good Afternoon".

import datetime
from zoneinfo import ZoneInfo

hyderabad_tz = ZoneInfo("Asia/Kolkata")

# Get the current datetime in Hyderabad
current_datetime_hyd = datetime.datetime.now(tz=hyderabad_tz)

# Extract only the time component
current_time_only = current_datetime_hyd.time()

noon_time = datetime.time(12, 0, 0) # hour=12, minute=0, second=0

if current_time_only > noon_time:
    print('Good Afternoon')
else:
    print('Good Morning')

'''
output
--------------
Good Afternoon

Process finished with exit code 0
'''
