#Generate a Python list of all the even numbers between 6 to 50
start, end = 6,51
for n in range(start, end):
    if n % 2 == 0:
        print(n,"\t")
