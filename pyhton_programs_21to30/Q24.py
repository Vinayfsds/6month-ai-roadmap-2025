#Write a program to determine whether a triangle is equilateral, isosceles, or
#scalene.

input_first_side = int(input('Enter the first side : '))
input_second_side = int(input('Enter the second side : '))
input_third_side = int(input('Enter the third side : '))

if input_first_side == input_second_side == input_third_side:
    print('It is equilateral triangle')
elif input_first_side == input_second_side or  input_second_side == input_third_side or input_first_side == input_third_side:
    print('It is a isosceles triangle')
else:
    print('It is a scalene triangle')

'''
Enter the first side : 10
Enter the second side : 10
Enter the third side : 10
It is equilateral triangle

Enter the first side : 15
Enter the second side : 10
Enter the third side : 15
It is a isosceles triangle

Enter the first side : 15
Enter the second side : 17
Enter the third side : 35
It is a scalene triangle
'''