#Find the grade of a student based on marks (90+ A, 80-89 B, etc.).

input_marks = int(input('Enter the marks of the student :'))

if input_marks > 90:
    print('Student got A grade.')
elif input_marks > 80 and input_marks < 90:
    print('Student got B grade.')
else:
    print('Student got C grade.')

'''
output
---------
Enter the marks of the student :99
Student got A grade.

Enter the marks of the student :89
Student got B grade.

Enter the marks of the student :79
Student got C grade.
'''