# . Find if a given number is exactly divisible by both 3 and 7.

input_number  = int(input('Enter a number : '))

message = f'Entered number {input_number} is not divisible by both 3 and 7'

if input_number % 3 == 0 and input_number % 7 == 0:
    message = f'Entered number {input_number} is divisible by both 3 and 7'

print(message)

'''
output
----------
Enter a number : 21
Entered number 21 is divisible by both 3 and 7

Enter a number : 9
Entered number 9 is not divisible by both 3 and 7
'''