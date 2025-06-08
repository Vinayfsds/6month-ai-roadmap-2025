#Check if a triangle is valid given three side lengths (sum of any two sides must
#be greater than the third).


a = int(input('Enter a : '))
b = int(input('Enter b : '))
c = int(input('Enter c : '))

if a + b >= c:
    print('It is a valid triangle')
else:
    print('It is invalid triangle')

'''
output
-------
Enter a : 8
Enter b : 8
Enter c : 16
It is a valid triangle

Enter a : 8
Enter b : 8
Enter c : 24
It is invalid triangle


'''