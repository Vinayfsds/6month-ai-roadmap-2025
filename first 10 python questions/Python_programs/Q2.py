# Check if a person is eligible to vote (age 18 or above).

user_age = int(input('Enter user age : '))

message ='User is not eligible to vote'
if (user_age >= 18):
    message  = 'User is eligible to vote'
print(message)

'''
output
--------
Enter user age : 12
User is not eligible to vote
'''