# Python Interview Questions

## 1.How can you improve the following code?

```py
import string

i = 0
for letter in string.letters:
    print("The letter at index %i is %s" % (i, letter))
    i = i + 1
```

## Answer

```py

import string

for index,letter in enumerate(string.ascii_letters):    
    print(f'The letter at index {index} is {letter}')

```

* Enumerate metodu key-value şəklində tuple qaytarır. Format string isə string'in içərisində dəyişən istifadə etmək üçün əlverişlidir.

## 2.What will be the output of the code below?

```py
List = ['a', 'b', 'c', 'd', 'e']
print(List[10:])
```

## Answer

* Bu metodla listin 10-cu indeksdən sonrakı elementlərini çap etmək istədiyimizi bildiririk. Lakin, listdə 5 element olduğu üçün 4-cü indeksdən sonra boş list qaytarır. Bu səbəbdən, 10-cu indeksdən sonrakı elementləri istədikdə bizə boş list ("[]") qaytarır.

## 3.What is a method?

```py
class Math:
    def multiplication(self, arg):
        return arg*2
    
multi = Math()

print(multi.multiplication(5))
```

## Answer

* Metod adətən, "multi.multiplication(arg)" şəklində çağırdığımız multi obyektində funksiyadır. Ümumiyyətlə, metodlar class daxilindəki funksiyalara deyilir.


## 4.How will you remove last object from a list?

`list.pop(obj=list[-1])` − pop metodu siyahıdan sonuncu elementi silir.



