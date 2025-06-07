# Write a program to find the greatest of two numbers.

number_1 = int(input('Enter number1 : '))

number_2 = int(input('Enter number2 : '))

if number_2 > number_1:
    print(f'Entered number {number_2} is greater than the number {number_1}')
elif number_1 > number_2:
    print(f'Entered number {number_1} is greater than the number {number_2}')
else:
    print('Both are equal')

'''
output
------
Enter number1 : 3
Enter number2 : 5
Entered number 5 is greater than the number 3
'''