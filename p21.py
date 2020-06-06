ch = input("Enter an Lowercase Character:\t")

if(ch>='a' and ch<='z'):
    i = ord(ch) - 32
    print("Converted Character:\t", chr(i))

else:
    print("Invalid Input")
