#  to check  whether character is Alphabet or not
char = input("Enter Your Character : ")
if((char >= 'a' and char<= 'z') or (char >= 'A' and char <= 'Z')):
    print("The Entered Character ", char, "is an Alphabet")
else:
    print("The Entered Character ", char, "is Not an Alphabet")
