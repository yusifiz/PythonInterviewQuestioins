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