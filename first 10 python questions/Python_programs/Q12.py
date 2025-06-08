# Verify if a number is a perfect square.

import math

input_number = int(input("Enter a number: "))

message = f'Entered number {input_number} is not a perfect square'

if (math.sqrt(input_number).is_integer()):
    message = f'Entered number {input_number} is a perfect square'

print(message)

'''
output:
--------

Enter a number: 25
Entered number 25 is a perfect square

Enter a number: 5
Entered number 5 is not a perfect square

'''
