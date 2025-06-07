# Check if a number is positive, negative, or zero

input_number = int(input('Enter your number : '))

if (input_number > 0):
    print(f'Entered number {input_number} is a positive number ')
elif (input_number < 0):
    print(f'Entered number {input_number} is a negative number ')
else:
    print(f'Entered number {input_number} is equals to zero')


'''
output
------
Enter your number : -10
Entered number -10 is a negative number 


Enter your number : 19
Entered number 19 is a positive number 
'''