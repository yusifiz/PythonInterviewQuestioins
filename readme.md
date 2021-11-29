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


## Answer

* `list.pop(obj=list[-1])` − pop metodu siyahıdan sonuncu elementi silir.


## 5.Write a sorting algorithm for a numerical dataset in Python.


## Answer

* Nümunədəki kodu izləyərək, python'da list'i sıralaya bilərsiniz.

```py
list = [-1, 4, 0,34, 6, -8]
list = [i for i in list]
list.sort()
print(list)
```

## 6.What is map function in Python?


## Answer

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


## Answer

* TkInter Python kitabxanasıdır. GUI (graphical user interface) üçün toolkit'dir (alət). Əsasən, masaüstü proqramları üçün istifadə olunur. Rənglər, şriftlər, ölçülər və kursorlar kimi atributları mövcuddur.


## 8.Is Python object oriented? what is object oriented programming?


## Answer

* Bəli, python obyekt yönümlü proqramlaşdırma dilidir. OOP class'lara və obyektlərə əsaslanan proqramlaşdırma paradiqmasıdır. OOP xüsusiyyətləri bunlardır: Encapsulation, Data Abstraction, Inheritance, Polymorphism.
 

## 9.Write a Python function that checks whether a passed string is palindrome Or not?


## Answer

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


## Answer

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

## Answer

* TypeError error'u verəcək çünki, map()'in len() funksiyası yoxdur. Yəni uzunluq anlayışı yoxdur.


## 12.What is the output of the following?

```py
x = ['ab', 'cd']
print(len(list(map(list, x))))
```

## Answer

* List'də 2 element olduğu üçün len() metodunun köməyi ilə, list'in uzunluğunu 2 alacayıq.


## 13.What is a dictionary in Python?


## Answer

* Dictionary (lüğət) python data tiplərindən biridir. Key - value (açar - dəyər) şəklində təyin edilir. Məsələn, işçi və onun maaşını nümunə göstərmək olar. 
``` 
dict={'Employee1':'1000','Employee2':'1500','Employee3':'2000'}

print(dict)
```
Output - <class 'dict;>

* Bu nümunədə key - employee, value - salary'dir.


## 14.How do you get a list of all the keys in a dictionary?


## Answer

* Bunun üçün key() metodundan istifadə edəcəyik.

```py
mydict={'a':1,'b':2,'c':3,'e':5}
mydict.keys()
print(dict_keys)
```

Output - (['a', 'b', 'c', 'e'])


## 15.Explain join() and split() in Python.


## Answer

* .join() metodu istənilən iterativ (sadalanan, list şəklində olan) elementi qəbul edir və onları müəyyən edilmiş simvolla ayırmağa kömək edir.

```','.join('12345')```

Output - '1,2,3,4,5' (string return edir.)

* .split() metodu təyin etdiyimiz simvol ətrafında string'ləri ayırır.

```'example@gmail.com'.split('@')```

Output - ['example', 'gmail.com'] (list içərisində simvola görə ayrılmış string'ləri return edir.)


## 16.What is the pass statement in Python?


## Answer

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


## Answer

Bunu etməyin iki yolu var:

```py
a,b,c=3,4,5     # Bu a=3, b=4, c=5 deməkdir.
a = b = c =3         # Bu isə göründüyü kimi hər 3 dəyişəni 3-ə bərabər edir.
```


## 18.What is tuple unpacking?


## Answer

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


## Answer

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

## Answer

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


## Answer 

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

* Pythonda yaddaş tənzimləmək üçün proqramda istifadə edilməyən obyektləri avtomatik olaraq silir. Bu proses Garbage Collection adlanır. Garbage collection hər bir obyekt üçün reference count (referans sayı) sayır. Və reference count 0-a bərabır olduğu zaman həmin obyekti silir. Obyektin referans sayı bu obyekt yeni bir dəyişənə ötürüldüyü zaman və ya list, tuple, dictionary-də istifadə olunduğu zaman artır. Obyektin referansları yenidən təyin edildiyi zaman və ya dəyişdirildiyi zaman isə reference count azalır.

```py

a = 100  // <100> obyekti yaranır

b = a // <100>-ün reference count-u artır

c = b // <100>-ün reference count-u artır

d = [a] // <100>-ün reference count-u artır

b = 50 // <100>-ün reference count-u azalır

d[0] = 30 // <100>-ün reference count-u azalır

``` 


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


## Answer


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


## Answer

1. Yeni başlayanlar üçün öyrənilməsi asan olan bir dildir.
2. Multi-purpose bir dildir. Yəni bir çox platforma üçün layihə hazırlamaq olur. Web app, desktop app, oyun, Aİ(suni intellekt) kimi bir fərqli sahələrdə istifadə oluna bilir.
3. Pythonun fərqli və geniş kitabxanasının olması developerlərə də rahatlıq təmin edir. Beləliklə developerlərin daha productive olmasına kömək edir.
4. Python developers community digər dillərə baxanda daha geniş yayıldığına görə bir məsələnin həllini tapmaq daha az vaxt alır.
5. OOPni dəstəklədiyinə görə hard codingdən bizi qoruyur. OOPnin bütün üstünlüklərini istifadə edə bilirik.


## 29. Mention what are the rules for local and global variables in Python?


## Answer

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


## 30. Suppose list1 is [2, 33, 222, 14, 25], What is list1[-1] ?


## Answer

* index olaraq -1 istifadə etdiyimiz zaman, listin ən sonuncu obyektini alırıq.

```py 
a = [2, 33, 222, 14, 25]
print(a[-1])

25

```


## 31. How would you randomize the contents of a list in-place?


## Answer

* Bunun üçün shuffle() funksiyasından istiffadə edilir. Öncəliklə bu funksiyanı import etmək lazımdır. İstifadəsi aşağıdakı kimidir.

```py

from random import shuffle

my_list = [1,2,3,5,6,88,54]

shuffle(my_list)

print(my_list)
```


## 32. Explain the //, %, and ** operators in Python.


## Answer

// Bölünmə zamanı nəticənin integer hissəsini göstərir.

```py

7 // 2

3

Normal bölünmə zamanı cavab 3.5 olmalı idi.
```

** Operatoru ədədin qüvvətini almaq üçündür. a üstü b almaq üçün a**b yazma lazımdır.

```py

2**10

1024
```

% Operatoru qalıqlı bölünmədə qalığı görmək üçün istifadə edilir.

```py

13 % 7 

6
```


## 33. What is a docstring?


## Answer

* Docstring hər hansı bit funsiyanın və ya metodun daxilində yazılır. Və həmin funksiya/metodun nə etdiyini açıqlayır. Docstringlər 3 ədəd tək/cüt dırnaq arasında yazılır.

```py

def salam():
    """
    Bu funskiya ekrana salam yazısını çıxarır
    """
    print("salam")

salam()

```

Funksiyanın docstringini görmək üçün __doc__ atributu istifadə edilir.

```py

print (salam.__doc__)

```


## 34. With Python, how do you find out which directory you are currently in?


## Answer

* Bunu tapmaq üçün getcwd() metodundan istifadə edilir. Öncəliklə os modulunu imoprt etməliyik.

```py

import os

os.getcwd()

'C:\Users\lifei\AppData\Local\Programs\Python\Python36-32'

```

Əlavə olaraq, chdir() metodu ilə bu direktoriyanı dəyişə də bilərik.

```py
os.chdir('C:\\Users\\lifei\\Desktop')
os.getcwd()

'C:\Users\lifei\Desktop'

```


## 35. How many arguments can the range() function take?


## Answer

* range() funksiyası 3 ədəd arqument götürür. Bunlar start, stop və step arqumentləridir. Start hansı ədəddən başlayacağını, stop hansı ədədə qədər davam edəcəyini, step isə artım ədədini bildirir. Step 2 olsa ədədlər iki - iki artacaqdır.

```py

range(5)

Yalnız 1 arqument verdikdə, funksiya bu ədədi stop arqumenti olaraq qəbul edir. Bu halda step 1 olur.

range(0,6)

İki arqument verdikdə birinci rəqəm start arqumenti, ikinci rəqəm isə stop arqumenti olur. Bu halda step yenə 1-ə bərabərdir.

range(0,20,2)

Üç arqument verdikdə isə birinci rəqəm start arqumenti, ikinci rəqəm isə stop arqumenti, üçüncü rəqəm isə step arqumenti olur.

```


## 36. What is the global keyword?


## Answer

* Global keywordü hansısa dəyişəni kodun istənilən yerində əlçatan etmək üçün istifadə edilir.

Misal üçün :

```py

 a=7
 def func():
    print(a)
    a+=1
    print(a)
```

Belə olan halda a is not defined erroru ilə qarşılaşacağıq. Erroru həll etmək üçün kodu aşağıdakı kimi dəyişməliyik :

```py

 a=7
 def func():
    global a
    print(a)
    a+=1
    print(a)
```


## 37. What functions or methods will you use to delete a file in Python?


## Answer

* remove() və unlink() metodlarından istifadə edə bilərik.

```py

import os
os.remove('app.py')
```

Unlinkin istifadəsi isə aşağıdakı kimidir.

```py 

import os 
os.unlink("app.py")
```


## 38.Illustrate the proper use of Python error handling.


## Answer

```py
try:    
    ….# Bura yoxlamaq istədiyiniz kodu yazırıq.
except:
    …# Yoxlamaq istədyiniz erroru və return'ü yazırıq.
finally:
    …# İstisnalara baxmayaraq, almaq istədiyiniz nəticəni bura yazırıq.
```


## 39.When would you use a break statement in a for loop?


## Answer

* For loop öz işini yerinə yetirdikdə və loop ilə bir işimiz qalmadıqda 'break' komandası köməyimizə çatır. Break bildirir ki, "mənim bu dövr ilə işim bitdi, növbəti kod blokuna keçin.".


## 40.Use a for loop and illustrate how you would define and print the characters in a string out, one per line.


## Answer

```py
myString = "I Love Python"
for myChar in myString:
    print(myChar)
```


## 41.Explain Inheritance in Python with an example.


## Answer

* Inheritance (varislik) bizə kodun təkrar istifadəsini təmin edir, proqram yaratmaq və saxlamağı asanlaşdırır. Bir class'a digər class'ın bütün atributlarını, metodlarını əldə etməyə kömək edir. Bu isə bizə eyni xüsusiyyətlərə sahib bir çox class'ı sadəcə bir dəfə yazaraq, digərləri ilə overwrite (üzərinə yazmaq) etməyə və ya yeni metod, atribut əlavə etməyə imkanı verir.


Python bir neçə fərqli tipdə inheritance'ı dəstəkləyir:

* Single Inheritance - bir class tək əsas class'dan inherit (miras) alır.

* Multi-level (çoxsəviyyəli) Inheritance - class A əsas class Base-dən inherit alır, həmçinin class B də class A-dan inherit alır.

* Hierarchical (ierarxik) inheritance – bir parent (valideyn) class'dan istənilən sayda child (uşaq) class inherit ala bilər.

* Multiple Inheritance - bir child class birdən çox parent class'dan inherit ala bilər.

* Hybrid Inheritance - iki və ya daha çox inheritance növünün birləşməsidir.


## 42.What is Hierarchical Inheritance?


## Answer

* Bir base (əsas) class'dan bir neçə derived (törəmə) class'ın inherit almasıdır.

```py
class Base(object):    
    def m1(self):       
        print("Base class'ında m1 funksiyası")

class A(Base):     
    def m2(self):   
        print("A class'ında m2 funksiyası")

class B(Base): 
    def m3(self):   
        print("B class'ında m3 funksiyası")
a1=A()
a1.m1()
a1.m2()
a=a1
print(a)
b1=B()
b1.m1()
b1.m3()
b=b1
print(b)
```
Output:

```
Base class'ında m1 funksiyası
A class'ında m2 funksiyası
<__main__.A object at 0x0000015AFF0BED00>
Base class'ında m1 funksiyası
B class'ında m3 funksiyası
<__main__.B object at 0x0000015AFF0BECD0>
```


## 43.What are negative indexes and why are they used?


## Answer

* Pythonda indekslər 0,müsbət və mənfi olur. 0 indeksi birinci elementi, 1 indeksi ikinci elementi və s. bildirir. Mənfi indekslərdə isə -1 indeksi sonuncu, -2 indeksi sonuncudan bir əvvəki və bu formada sondan başlayaraq davam edir.

* Məsələn, print(a[:-1]) yazsaq, sonuncu element daxil olmamaqla, sonuncu elementə qədər çap edəcək. print(a[::-1]) yazanda isə, tərsinə sıralayaycaq.

Bir list götürsək:

```
mylist=[0,1,2,3,4,5,6,7,8]
```

Mənfi indekslə bir elementi çap edəndə sonuncudan başlayaraq, sayacaq.

```
mylist[-3]
```
Output: 6 (sondan 3cü element)

Mənfi indekslə element aralığı çap etmək istədikdə:

```
mylist[-6:-1]
```
Output: [3, 4, 5, 6, 7] (sondan başlayaraq 6cı element daxil olmaqla, 1ci elementə qədər (1ci element daxil deyil) çap edəcək.)

Tərsinə sıralasaq:

```
mylist[::-1]
```
Output: [8,7,6,5,4,3,2,1,0]

`mylist[:-1]` isə sonuncu element daxil olmadan ona qədərki elementləri gətirəcək.



## 44.Explain a few methods to implement Functionally Oriented Programming in Python.


## Answer

Bir listdə fərqli məqsədlər üçün dövr etməyin bir neçə yolu var:

* `filter()`: list üzərində istədiyimiz elementləri filter etməyə imkan yaradır.

```py
list(filter(lambda x:x>5,range(8)))
```
Output: [6,7]

* `map()` : bu funksiya list'in hər bir elementinə funksiya tətbiq edir.

```py
list(map(lambda x:x**2,range(8)))
```
Output: [0, 1, 4, 9, 16, 25, 36, 49]


* `reduce()` : bir nəticə alana qədər elementləri azaldır.

```py
from functools import reduce

def sum(a, b):
    print(f"a={a}, b={b}, {a} + {b} ={a+b}")
    return a + b


scores = [75, 65, 80, 95, 50]
total = reduce(sum, scores)
print(total)
```
Output:
```
a=75, b=65, 75 + 65 = 140
a=140, b=80, 140 + 80 = 220
a=220, b=95, 220 + 95 = 315
a=315, b=50, 315 + 50 = 365
365
```
Lamda'dan istifadə edərək daha sadə yazsaq:

```py
from functools import reduce

scores = [75, 65, 80, 95, 50]

total = reduce(lambda a, b: a + b, scores)

print(total)
```
Output: 365


## 45.Explain split(), sub(), subn() methods of re module in Python.


## Answer

* Pythonda stringləri dəyişməyin bir neçə yolu var.

1. split() - bu method regex pattern'ə uygun olaraq verilmiş şərtə görə stringi bölür
2. sub() - bu methodda 2 parametr verilir, biri textdə dəyişmək istədiyiniz hissədir. Digəri isə dəyişmək istədiyiniz hissəyə nə qoymaq istəyirsiz.
3. subn() - bu method da eyni sub methodu kimi işləyir, eyni zamanda nə qədər dəyişiklik edibsə onun sayın da göstərir.


## 46.What are assignment operators in Python?


## Answer

Pythonda xüsusi simvollarla işlənən bəzi operatorlar vardır. Bunu nümunələrlə daha yaxşı anlamaq olar.

1. '+' operatoru.
```py
 a = 7
 a += 1
 a
```
Output: 8

2. '-' operatoru.
```py
 a = 7
 a -= 1
 a
```
Output: 6

3. '*' operatoru.
```py
 a = 7
 a*2
 a
```
Output: 14

4. '/' operatoru.
```py
 a = 14
 a/2
 a
```
Output: 7

5. '%' operatoru. (Bölmə zamanı qalığı göstərir)
```py
 a = 5
 a%2
 a
```
Output: 1

6. '//' operatoru. (Bölmə zamanı tam rəqəmi göstərir)
```py
 a = 5
 a//2
 a
```
Output: 2

7. '**' operatoru. (verilən rəqəmi qüvvətə yüksəldir.)
```py
 a = 5
 a**2
 a
```
Output: 25


## 47.What are membership, operators?


## Answer

* Bu operatorlar 'in' və 'not in' operatorlarıdır. Məsələn bir textdə hər hansısa bir hərfin, bir listdə hər hansısa bir elementin olub olmamasını yoxlamaq üçün istifadə edilə bilər.

```py
if 'y' in 'yusif':
    print(True)
```

Output: True

```py
if 'x' not in 'yusif':
    print(False)
```

Output: False


## 48.What is the concatenation?


## Answer

* Pythonda '+' operatoru ilə stringəri, listləri bir birinə birləşdirmək üçün istifadə olunur.

` '32'+'32' `
3232

` [1,2,3]+[4,5,6] `
[1, 2, 3, 4, 5, 6]

* Burda diqqət etməli olduğumuz mövzu fərqli ata tipdə olan valueları bir birilə birləşdirə bilmərik.

` (2,3)+(4)  # burda error verəcək çünki, 4 integer olduğu üçün list ilə birləşdirə bilmərik. `

* Bunun üçün aşağıdakı kimi yazmaq olar.

` (2,3)+(4,) `
(2, 3, 4)


## 49.How to retrieve data from a table in MySQL database through Python code?


## Answer

```py
#1. Mysql ilə əlaqə qurulur.

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

#2. Cursor obyekti yaranır

mycursor = mydb.cursor()

#3. Databazaya sorğu göndərilir

mycursor.execute("SELECT * FROM customers")

#4. Sorğuya uyğun seçdiyimiz datanı row şəklində bizə qaytarır.

myresult = mycursor.fetchall()

#5. Databaza əlaqəsi bağlanılır.

db.close()

```


## 50.Is Python case-sensitive?


## Answer

Bəli Python case-sensitive bir dildir. Bunu HTML ilə müqayisə edə bilərik. HTML'də `<p>` ilə `<P>` eyni mənanı verir. Yalnız Python böyük və kiçik hərfləri tanıdığı üçün 'number' variable'ni başqa yerdə istifadə edərkən 'Number' yazsanız Python error verəcək.


```py

#Yalnış nümunə

first_name = 'Tim'
last_name = 'Statler'

print('My name is ' + First_Name + ' ' + LAST_Name)

```

```py

# Doğru nümunə

first_name = 'Tim'
last_name = 'Statler'

print('My name is ' + first_name + ' ' + last_name)

```