# Determine if a number is between 1 and 100.

input_number = int(input('Enter a number: '))
message = f'Entered number {input_number} is not between 1 and 100'

if (input_number > 1) and (input_number < 100):
    message = f'Entered number {input_number} is between 1 and 100'

print(message)

'''
output
-------
Enter a number: 59
Entered number 59 is between 1 and 100

Enter a number: 101
Entered number 101 is not between 1 and 100
'''