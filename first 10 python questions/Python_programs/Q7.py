# Check if a character is a vowel or consonant.

list_vowels =['a','e','i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

input_char = input('Enter a character : ')
if input_char in list_vowels:
    print(f'Entered character {input_char} is vowel')
else:
    print(f'Entered character {input_char} is a consonant')

'''
output
-------
Enter a character : a
Entered character a is vowel
'''