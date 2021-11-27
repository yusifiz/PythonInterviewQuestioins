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


# Answer

* `list.pop(obj=list[-1])` − pop metodu siyahıdan sonuncu elementi silir.


## 5.Write a sorting algorithm for a numerical dataset in Python.


# Answer

* Nümunədəki kodu izləyərək, python'da list'i sıralaya bilərsiniz.

```py
list = [-1, 4, 0,34, 6, -8]
list = [i for i in list]
list.sort()
print(list)
```

## 6.What is map function in Python?


# Answer

* Map() funksiyası daxilində iterable obyekt və funksiya qəbul edir (Məs: map(func, iterable ...)).

Nümunə: 

```py
numbers = [2, 4, 6, 8, 10]

def square(number):
  return number * number

squared_numbers_iterator = map(square, numbers)

squared_numbers = list(squared_numbers_iterator)
print(squared_numbers)

# Output: [4, 16, 36, 64, 100]
```

## 7.What is TkInter?


# Answer

* TkInter Python kitabxanasıdır. GUI (graphical user interface) üçün toolkit'dir (alət). Əsasən, masaüstü proqramları üçün istifadə olunur. Rənglər, şriftlər, ölçülər və kursorlar kimi atributları mövcuddur.


## 8.Is Python object oriented? what is object oriented programming?


# Answer

* Bəli, python obyekt yönümlü proqramlaşdırma dilidir. OOP class'lara və obyektlərə əsaslanan proqramlaşdırma paradiqmasıdır. OOP xüsusiyyətləri bunlardır: Encapsulation, Data Abstraction, Inheritance, Polymorphism.
 

## 9.Write a Python function that checks whether a passed string is palindrome Or not?


# Answer

```py
def palindrome(string):
    left_pos = 0
    right_pos = len(string) – 1

    while right_pos >= left_pos:
        if not string[left_pos] == string[right_pos]:
            return False

    left_pos += 1
    right_pos -= 1
    return True
print(palindrome('ana'))
```

* Qeyd: Palindrom, tərsdən yazılışı da eyni cür olan sözlərə deyilir (Məs: ana, ata)


## 10.Write a Python program to calculate the sum of a list of numbers.


# Answer

```py
def list_sum(num_List):
    if len(num_List) == 1:
        return num_List[0]
    else:
        return num_List[0] + list_sum(num_List[1:])
print(list_sum([1, 2, 3, 4, 5]))
```
Output: 15


## 11.What is the output of the following?

```py(
x = ['ab', 'cd']
print(len(map(list, x)))
```

# Answer

* TypeError error'u verəcək çünki, map()'in len() funksiyası yoxdur. Yəni uzunluq anlayışı yoxdur.


## 12.What is the output of the following?

```py
x = ['ab', 'cd']
print(len(list(map(list, x))))
```

# Answer

* List'də 2 element olduğu üçün len() metodunun köməyi ilə, list'in uzunluğunu 2 alacayıq.


## 13.What is a dictionary in Python?


# Answer

* Dictionary (lüğət) python data tiplərindən biridir. Key - value (açar - dəyər) şəklində təyin edilir. Məsələn, işçi və onun maaşını nümunə göstərmək olar. 
``` 
dict={'Employee1':'1000','Employee2':'1500','Employee3':'2000'}

print(dict)
```
* Output - <class 'dict;>

* Bu nümunədə key - employee, value - salary'dir.


## 14.How do you get a list of all the keys in a dictionary?


# Answer

* Bunun üçün key() metodundan istifadə edəcəyik.

```py
mydict={'a':1,'b':2,'c':3,'e':5}
mydict.keys()
print(dict_keys)
```

* Output - (['a', 'b', 'c', 'e'])


