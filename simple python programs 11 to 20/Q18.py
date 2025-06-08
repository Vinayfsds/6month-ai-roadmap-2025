# . Check if a number is divisible by 2 but not by 3.

input_number  = int(input('Enter a number : '))

message = f'Entered number {input_number} is not divisible by both 2 and 3'

if input_number % 2 == 0 and input_number % 3 == 0:
    message = f'Entered number {input_number} is divisible by both 2 and 3'

print(message)

'''
output
----------
Enter a number : 6
Entered number 6 is divisible by both 2 and 3

Enter a number : 21
Entered number 21 is not divisible by both 2 and 3
'''