print("Enter Marks of student: ")
mark=int(input())
if mark<25:
    print("Your Grade is F")
elif mark>25 and mark<45:
    print("Your Grade is E ")
elif mark>45 and mark<50:
    print("Your Grade is D ")
elif mark>50 and mark<60:
    print("Your Grade is C")
elif mark>60 and mark<80:
    print("Your Grade is B ")
elif mark>80:
    print("Your Grade is A ")
else:
    print("Invalid Input!")
