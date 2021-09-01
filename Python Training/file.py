


f=open(r"Desktop/xyz.txt","r")
print("Properties of a file:")
print("File name",f.name)
print("File mode",f.mode)
print("Is closed:",f.closed)
print("Is readable:",f.readable())
print("Is writable:",f.writable())
f.close()
print("Is closed:",f.closed)

#writing data in a file
f=open(r"Desktop/xyz.txt","w")
f.write("File\n")
f.write("Handling\n")
f.write("In Python\n")
print("Your data entered successfully")
#write data by passing list
f.write("\nData types in python:\t")
list=["number\t","string\t","tuple\t","list\t","set\t","dictionary\t"]
f.writelines(list)
print("List entered successfully")
f.close()

#Reading character from text file
#Read total data
f=open(r"Desktop/xyz.txt","r")
print("Data in file is:\n")
d=f.read()
print(d)
#Reading specific 
f.read(10)
l=f.readline()
print(l,end="")
f.close()
