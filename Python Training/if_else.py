print("Enter ages of 3 peoples:")
age1=int(input("Enter first person's age"))
age2=int(input("Enter second person's age"))
age3=int(input("Enter third person's age")) 
if(age1>age2 and age1>age3):
  print(age1,"is oldest")
elif (age2>age1 and age2>age3):
  print(age2,"is oldest")
elif(age3>age1 and age3>age2):
  print(age3,"is oldest")

if(age1<age2 and age1<age3):
  print(age1,"is youngest")
elif (age2<age1 and age2<age3):
  print(age2,"is youngest")
elif(age3<age1 and age3<age2):
  print(age3,"is youngest")
