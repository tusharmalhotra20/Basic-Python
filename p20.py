#WAP to input UpperCase Character and convert it into LowerCase Character.

ch = input("Enter an UpperCase Character:\t")

if (ch>='A' and ch<='Z'):
    i = ord(ch) + 32
    print("Converted Character:\t", chr(i))

else:
    print("Invalid Input")
