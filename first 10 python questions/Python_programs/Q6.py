# Determine if a number is a multiple of 5.

number = int(input('Enter number : '))

if number % 5 ==0:
    print(f'Entered number {number} is multiple of 5')
else:
    print(f'Entered number {number} is not multiple of 5')

'''
output
-------
Enter number : 25
Entered number 25 is multiple of 5
'''