#Determine if a given alphabet is uppercase or lowercase
from soupsieve.util import lower

input_alphabet = input('Enter a alphabet : ')

if (input_alphabet.islower()):
    print('Entered alphabet is lower')
else:
    print('Entered alphabet is upper')

'''

output
------------------

Enter a alphabet : V
Entered alphabet is upper
'''