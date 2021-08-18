#####operators#####
#1.Arithmetic operator
a=10
b=2
print("Addition is:",a+b)
print("Subtrction is:",a-b)
print("Multiplication is:",a*b)
print("Division  is:",a/b)
print("Exponential is:",a**b)
print("Remainder is:",a%b)
print("Ronded division is:",a//b)

#2.Assignment operator
a=20
print("Value of a is:",a)
a+=20
print("a will increment by 20:",a)
a-=20
print("a will decrement by 20:",a)
a*=20
print("a will multiplied by 20:",a)
a/=20
print("a will divided by 20:",a)
a%=20
print("a will moduled by 20:",a)

#3.Comparison operator(on integers)
a=2
b=4
print(a==2)
print(b==2)
print(a!=b)
print(a>b)
print(a<b)
#(on strings)
a="pop"
b="oop"
print(a=="pop")
print(b=="pop")
print(a!=b)
print(a>b)
print(a<b)

#logical operator
a=True
b=False
print(a and a)
print(a and b)
print(a or b)

#Identity operators
a=True
b=False
print(a is b)
print(a is not b)

#Membership operators
list=[1,2,3,4]
print(1 in list)
print(5 in list)
print(1 not in list)
print(5 not in list)

#Bitwise operator
a=30
b=20
c=a&b#bitwise AND
print(c)
a=30
b=20
c=a|b#Bitwise OR
print(c)
a=30
b=20
c=a^b#Bitwise XOR
print(c)
a=30
b=~a#Bitwise NOT
print(b)
