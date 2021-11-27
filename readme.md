# Python Interview Questions

## 1.How can you improve the following code?

```py
import string

i = 0
for letter in string.letters:
    print("The letter at index %i is %s" % (i, letter))
    i = i + 1
```

### Answer

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

### Answer

* Bu metodla listin 10-cu indeksdən sonrakı elementlərini çap etmək istədiyimizi bildiririk. Lakin, listdə 5 element olduğu üçün 4-cü indeksdən sonra boş list qaytarır. Bu səbəbdən, 10-cu indeksdən sonrakı elementləri istədikdə bizə boş list ("[]") qaytarır.

## 3.What is a method?

```py
class Math:
    def multiplication(self, arg):
        return arg*2
    
multi = Math()

print(multi.multiplication(5))
```

### Answer

* Metod adətən, "multi.multiplication(arg)" şəklində çağırdığımız multi obyektində funksiyadır. Ümumiyyətlə, metodlar class daxilindəki funksiyalara deyilir.


## 4.How will you remove last object from a list?


### Answer

* `list.pop(obj=list[-1])` − pop metodu siyahıdan sonuncu elementi silir.


## 5.Write a sorting algorithm for a numerical dataset in Python.


### Answer

* Nümunədəki kodu izləyərək, python'da list'i sıralaya bilərsiniz.

```py
list = [-1, 4, 0,34, 6, -8]
list = [i for i in list]
list.sort()
print(list)
```

## 6.What is map function in Python?


### Answer

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


### Answer

* TkInter Python kitabxanasıdır. GUI (graphical user interface) üçün toolkit'dir (alət). Əsasən, masaüstü proqramları üçün istifadə olunur. Rənglər, şriftlər, ölçülər və kursorlar kimi atributları mövcuddur.


## 8.Is Python object oriented? what is object oriented programming?


### Answer

* Bəli, python obyekt yönümlü proqramlaşdırma dilidir. OOP class'lara və obyektlərə əsaslanan proqramlaşdırma paradiqmasıdır. OOP xüsusiyyətləri bunlardır: Encapsulation, Data Abstraction, Inheritance, Polymorphism.
 

## 9.Write a Python function that checks whether a passed string is palindrome Or not?


### Answer

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


### Answer

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

### Answer

* TypeError error'u verəcək çünki, map()'in len() funksiyası yoxdur. Yəni uzunluq anlayışı yoxdur.


## 12.What is the output of the following?

```py
x = ['ab', 'cd']
print(len(list(map(list, x))))
```

### Answer

* List'də 2 element olduğu üçün len() metodunun köməyi ilə, list'in uzunluğunu 2 alacayıq.


## 13.What is a dictionary in Python?


### Answer

* Dictionary (lüğət) python data tiplərindən biridir. Key - value (açar - dəyər) şəklində təyin edilir. Məsələn, işçi və onun maaşını nümunə göstərmək olar. 
``` 
dict={'Employee1':'1000','Employee2':'1500','Employee3':'2000'}

print(dict)
```
Output - <class 'dict;>

* Bu nümunədə key - employee, value - salary'dir.


## 14.How do you get a list of all the keys in a dictionary?


### Answer

* Bunun üçün key() metodundan istifadə edəcəyik.

```py
mydict={'a':1,'b':2,'c':3,'e':5}
mydict.keys()
print(dict_keys)
```

Output - (['a', 'b', 'c', 'e'])


## 15.Explain join() and split() in Python.


### Answer

* .join() metodu istənilən iterativ (sadalanan, list şəklində olan) elementi qəbul edir və onları müəyyən edilmiş simvolla ayırmağa kömək edir.

```','.join('12345')```

Output - '1,2,3,4,5' (string return edir.)

* .split() metodu təyin etdiyimiz simvol ətrafında string'ləri ayırır.

```'example@gmail.com'.split('@')```

Output - ['example', 'gmail.com'] (list içərisində simvola görə ayrılmış string'ləri return edir.)


## 16.What is the pass statement in Python?


### Answer

* Kodumuza hələ nə edəcəyimizə qərar vermədiyimiz vaxtlar ola bilər. Bu zaman kodun düzgün sintaksı olması üçün (error verməməsi üçün), 'pass' ifadəsindən istifadə edə bilərik.

```py
def func(*args):
    pass 
```

* Eyni ifadəyə "..." şəklində rast gələ bilərsiniz.

```py
def func(*args):
    ... 
```


## 17.How can you declare multiple assignments in one statement?


### Answer

Bunu etməyin iki yolu var:

```py
a,b,c=3,4,5     # Bu a=3, b=4, c=5 deməkdir.
a = b = c =3         # Bu isə göründüyü kimi hər 3 dəyişəni 3-ə bərabər edir.
```


## 18.What is tuple unpacking?


### Answer

* Tuple bir sıra dəyərləri (values) bir siyayıda toplamaq üçün istifadə olunur. List'dən fərqi içindəki elementləri kənardan dəyişmək olmur, sabit siyahı formasıdır. 

```py
mytuple=3,4,5
print(mytuple)
```

Bu nümunədə 3,4,5 ədədlərini tuple'a əlavə edirik.

```py
x,y,z=mytuple
print(x+y+z)
```

Burada isə tuple'a atdığımız integer dəyərləri x,y,z dəyişənlərinə mənimsədirik.


## 19.What data types does Python support?


### Answer

* Python bizə 5 növ data tipi təqdim edir.

```py
     a=7.0
     title="Ramayan's Book"
     colors=['red','green','blue']
     type(colors)
        <class 'list'>
     name=('Ramayan','Sharma')
     name[0]='Avery'
        Traceback (most recent call last):
        File "<pyshell#129>, line 1, in <module> name[0]='Avery'
        TypeError: 'tuple' object does not support item assignment # tuple kənardan dəyişdirilə bilmədiyi üçün TypeError verir.
     squares={1:1,2:4,3:9,4:16,5:25}
     type(squares)
        <class 'dict'>
     type({})
        <class 'dict'>
     squares={x:x**2 for x in range(1,6)}
     squares
        {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```


## 20.What is slicing?

### Answer

Slice() metodu bizə stringi və ya list elementlərini hissələrə ayırmaq üçün istifadə olunur.

```py
  (1,2,3,4,5)[2:4]
        (3, 4)
     [7,6,8,5,9][2:]
        [8, 5, 9]
     'Hello'[:-1]
        'Hell'
```


## 21. How do I convert a number to a string?


### Answer 

Pythonda number data tipini string data tipinə dəyişməyin bir neçə yolu var.
str(), "%s" , "f-string" , format()  kimi methodlardan istifadə oluna bilər

###  str() function istifadəsi

```py 

num = 10

print(type(num))

converted_num = str(num) 

print(type(converted_num))

```

###   “%s” keyword istifadəsi

```py 


num = 10
 
print(type(num))
 
converted_num = "% s" % num
print(type(converted_num))

```

###   f-string`in istifadəsi

```py 
num = 10

print(type(num))
 
converted_num = f'{num}'
 
print(type(converted_num))

```

###  .format() function istifadəsi

```py 

num = 10
 
print(type(num))
 
converted_num = "{}".format(num)
print(type(converted_num))

```


## 22. What is Garbage Collection?


## Answer

* Pythonda Garbage Collection istifadə olunmayan obyektlərin depolanması üçün bir yerdir. Bu funksiya uzun müddət istifadə olunmayan obyektləri siradan çıxarır və yaddaşda yeni obyektlər üçün yer açır. Bunu komputerdə  recycling system(yenidən emal) prosesi kimi təsəvvür edə bilərsiniz. 


## 23. How do you create your own package in Python?


## Answer

1. Əvvəlcə directory yaradırıq və ona package name veririk
2. Sonra ora lazım olan funksiyaları və classları yerləşdiririk.
3. Sonunda isə directory`nin içində init.py faylı yaradırıq ki, Python bu directory-nin  package olduğunu anlasın.


## 24. Explain the use "with" statement in python?


## Answer

"With" statement kodların daha oxunaqlı və təmiz olmasında önəmli rol oynayır. Bunun yanı sıra, faylların idarə olunmasına da köməklik edir. Aşağıdakı kod parçasında bunun nümunısini görə bilərik.

```py 

# 1) with statementdən istifadə edilmədikdə
file = open('file_path', 'w')
file.write('hello world !')
file.close()
  
# 2) with statementdən istifadə edilmədikdə
file = open('file_path', 'w')
try:
    file.write('hello world')
finally:
    file.close()

  
# with statementdən istifadə edildikdə
with open('file_path', 'w') as file:
    file.write('hello world !')

```


## 25. Mention the use of the split function in Python?


## Answer

Pythonda split() methodu listləri verilmiş şərtə əsasən bölür. Default olaraq(Əgər şərt verilməsə) listləri boşluğa əsasən bölür. Aşağıdakı nümunədə necə işlədiyini görmək olar.

```py 

text = 'geeks for geeks'
  
# boşluğa əsasən bölür
print(text.split())
  
word = 'geeks, for, geeks'
  
# Vergülə əsasən bölür
print(word.split(','))
  
word = 'geeks:for:geeks'
  
# Qoşa nöqtəyə əsasən bölür
print(word.split(':'))
  
word = 'CatBatSatFatOr'
  
# t hərfinə əsasən bölür
print(word.split('t'))

```


## 26. How do you take input in Python?


## Answer

* Pythonda input üçün input() funksiyasından istifadə olunur. Userdən hər hansısa bir datanı götürmək üçün istifadə olunur. Məsələn age = input("Yaşınızı qeyd edin: ")  formasında yazsaq userdən gələn datanı bir dəyərə bərabər edə bilirik. Bir nüansı qeyd etmək lazımdır ki, input() methodu string qaytarır, əgər int qaytarmasını istəyirsinizsə age = int(input("Yaşınızı qeyd edin: ")) kimi yaza bilərsiniz.


## 27. Explain logical operators in Python.


### Answer


Bir çox programlaşdırma dilində olduğu kimi Pythonda da 3 dənə logical operator var. And , Or, Not.

### 1. And operator 
* Bu operatorla verilən bütün şərtlər ödənməlidir.
  
```py 

a = 10
b = 10
c = -10
  
if a > 0 and b > 0:
    print("The numbers are greater than 0")
  
if a > 0 and b > 0 and c > 0:
    print("The numbers are greater than 0")
else:
    print("Atleast one number is not greater than 0")

```

### Nəticə 

```
The numbers are greater than 0

Atleast one number is not greater than 0
```
### 2. Or operator 
* Bu oparetorla verilən statementlar bir şərt ödəndikdə işləyir.

```py 

a = 10
b = -10
c = 0
  
if a > 0 or b > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")
  
if b > 0 or c > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")

```

### Nəticə 

```

Either of the number is greater than 0
No number is greater than 0

```

### 3. Not operator 
* Pythonda Not operatoru boolean valuelarla işlənir. Məsələn boolean value True-dursa, bu False qaytarır.

```py 
a = 10
  
if not a:
    print("Boolean value of a is True")
  
if not (a%3 == 0 or a%5 == 0):
    print("10 is not divisible by either 3 or 5")
else:
    print("10 is divisible by either 3 or 5")

```

### Nəticə

``` 
10 is divisible by either 3 or 5

```


## 28. Mention five benefits of using Python?


### Answer

1. Yeni başlayanlar üçün öyrənilməsi asan olan bir dildir.
2. Multi-purpose bir dildir. Yəni bir çox platforma üçün layihə hazırlamaq olur. Web app, desktop app, oyun, Aİ(suni intellekt) kimi bir fərqli sahələrdə istifadə oluna bilir.
3. Pythonun fərqli və geniş kitabxanasının olması developerlərə də rahatlıq təmin edir. Beləliklə developerlərin daha productive olmasına kömək edir.
4. Python developers community digər dillərə baxanda daha geniş yayıldığına görə bir məsələnin həllini tapmaq daha az vaxt alır.
5. OOPni dəstəklədiyinə görə hard codingdən bizi qoruyur. OOPnin bütün üstünlüklərini istifadə edə bilirik.


## 29. Mention what are the rules for local and global variables in Python?


### Answer

* Funksiyaların içində yaranan hər bir variable (məs: x=3) local variable sayılır. Onun istifadəsi və icazəsi yalnız həmin funksiya üçün olur. 

```py 
def foo():
    y = "local"
    print(y)

foo()

```

* Nəticə 
  
```
local
```

* Məsələn yuxarıdakı kod parçasına baxdıqda y dəyəri funksiyanın içində yaranıb və içində də istifadə olunur. Əgər print funksiyası funsiyanın çölündə icra olunsaydı kod error verecekdi.

## Global Value

* Bu o variabledir ki funksiyanın çölündə də yaransa da onu bütün funksiyalarda istifadəsi mümkündür.

```py 

x = "global"

def foo():
    print("x inside:", x)


foo()
print("x outside:", x)


```
* Nəticə 

```
x inside: global
x outside: global

```

* Bu misalda isə x global variable olduğu üçün həm funksiyanın içində həm də çölündə istifadəsi mümkündür.ad

