#Finding average of n elements using while loop
print("Enter how many no. of elements u required for finding average: ")
n=int(input())
sum=0
count=0

print("\nNow enter the elements: ")

#Taking elements nd finding sum
while(count<n):
  i=int(input())
  sum=sum+i
  count+=1
#finding average
avg=sum/n
#printing average
print(f"\nAverage is: {avg}")
