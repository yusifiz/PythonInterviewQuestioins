# Python Interview Questions

## How can you improve the following code?

'''py
import string

i = 0
for letter in string.letters:
    print("The letter at index %i is %s" % (i, letter))
    i = i + 1
'''

* Enumerate metodu key-value şəklində tuple qaytarır. Format string isə string'in içərisində dəyişən istifadə etmək üçün əlverişlidir.

'''py

import string

for index,letter in enumerate(string.ascii_letters):    
    print(f'The letter at index {index} is {letter}')

'''