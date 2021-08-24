n= int(input("Enter a number for finding the factorial: "))    
fact = 1    
if n < 0:    
   print("There is no factorial for negative numbers.")    
elif n == 0:    
   print("The factorial of 0 is 1")    
else:    
   for i in range(1,n + 1):    
       fact = fact*i    
   print("The factorial of",n,"is",fact)    
