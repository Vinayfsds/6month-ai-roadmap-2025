#Check if a person is eligible for a driving license (age 18+, passed the driving
#test)

input_age = int(input('Enter the person age : '))
test_passed = bool(input('test passed 1 - yes and 0 - no : '))
if input_age >= 18 and test_passed:
    print('Person eligible for driving license')
else:
    print('Person not eligible for driving license')

'''
output
-------
Enter the person age : 25
test passed 1 - yes and 0 - no : 1
Person eligible for driving license
'''