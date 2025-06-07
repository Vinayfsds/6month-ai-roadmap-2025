# Determine if a given year is a leap year or not.
input_year = int(input('Enter a year : '))

message = f'Entered year {input_year} is not a leap year'

if (input_year % 4 == 0):
    message = f'Entered year {input_year} is a leap year'

print(message)

'''
Enter a year : 2026
Entered year 2026 is not a leap year
'''