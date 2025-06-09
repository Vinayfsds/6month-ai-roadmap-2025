# Find the largest of three numbers

a = int(input('Enter the input a : '))
b = int(input('Enter the input b : '))
c = int(input('Enter the input c : '))

list_values = []
list_values.append(a)
list_values.append(b)
list_values.append(c)
list_values.sort(reverse=True)

print(f'The larget of three numbers : {list_values[0]}')

'''
output
------------
Enter the input a : 33
Enter the input b : 22
Enter the input c : 78
The larget of three numbers : 78
'''