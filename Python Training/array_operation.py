from array import *

a = array('i', [90, 80, 30]) #declaration
print(a)
print(a[2])   
a.append(40) 
print(a)
a.insert(2, 45) 
print(a)
a.extend([50, 60, 70])
print(a)
b = array('i', [1, 2, 3])
c = a + b
print("Concatinated array:", c)
c.pop()
print(c)
c.remove(45)
print(c)
print(c[0:5])
