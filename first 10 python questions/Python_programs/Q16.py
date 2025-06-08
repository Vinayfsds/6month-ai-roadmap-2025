# Check if the sum of two numbers is greater than 100
first_number = int(input('Enter your first number : '))
second_number = int(input('Enter your second number : '))

if (first_number + second_number) > 100:
    print(f'Entered values are greater than 100')
else:
    print(f'Entered values are less than or equals 100')

'''
output
-----------
Enter your first number : 98
Enter your second number : 4
Entered values are greater than 100
'''