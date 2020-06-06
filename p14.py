a = float(input("Enter first number:\t"))
b = float(input("Enter second number:\t"))
c = float(input("Entre third number:\t"))

if (a>=b) and (a>=c):
    lnum = a
elif (b>=a) and (b>=c):
    lnum = b
else:
    lnum = c

print("The largest number among",a,",",b,"and",c,"is: ",lnum)
