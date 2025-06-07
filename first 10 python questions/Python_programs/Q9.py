# Write a program to check if a number is a single-digit number.

input_number = int(input('Enter a number : '))

if (input_number < 10) and (input_number < -10):
    print(f'Entered number {input_number} is a single-digit number')
else:
    print(f'Entered number {input_number} is a double-digit number')

'''
output
-------
Enter a number : 5
Entered number 5 is a double-digit number
'''