#Determine if a person is eligible for a senior citizen discount (age 60+).

age= int(input('Enter age : '))

if age > 60:
    print(f'Person is eligible for a senior citizen discount')
else:
    print(f'Person is not eligible for a senior citizen discount')

'''
output
---------
Enter age : 65
Person is eligible for a senior citizen discount
'''