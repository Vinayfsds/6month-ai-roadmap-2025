#Check if a number is a palindrome (same forward and backward).

input_number = int(input('Enter a number : '))


if int(str(input_number)[::-1]) == input_number:
    print('Entered number is a palindrome!!')
else:
    print('Entered number is not a palindrome!!')

'''
output
--------
Enter a number : 1331
Entered number is a palindrome!!

Enter a number : 12331
Entered number is not a palindrome!!
'''

