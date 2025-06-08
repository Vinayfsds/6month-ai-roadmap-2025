# Check if a string is empty or not.

input_string = input(f'Enter the user input : ')
message = 'user input is empty'

if (input_string != ''):
    message = f'user has entered - \'{input_string}\''


print(message)

'''

output
---------
Enter the user input : 
user input is empty

Enter the user input : Vinay
user has entered - 'Vinay

'''

