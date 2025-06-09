#Determine if a given date is valid (considering month length and leap year for
#February).

input_date = input('Enter a date :')

day = input_date.split('-')[0]
month = input_date.split('-')[1]
year = input_date.split('-')[2]

if (len(day) >=1 and len(month) >=2 and len(year) >=4):
    if int(year)% 4 ==0 and int(day) <=29:
        print('It is a valid date')
    elif int(year)% 4 !=0 and int(day) <=28:
        print('It is a valid date')
    else:
        print('It is not a valid date')
else:
    print('It is not a valid date')

'''
output
--------
Enter a date :29-02-2024
It is a valid date

Enter a date :29-02-2026
It is not a valid date
'''