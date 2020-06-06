#WAP to print highest of three numbers using nested else-if.

a = float(input("Enter first number:\t"))
b = float(input("Enter second number:\t"))
c = float(input("Entre third number:\t"))

if a>=b:
    if a>=c:
        lnum = a
    else:
        lnum = c
if b>=a:
    if b>=c:
        lnum = b
    else:
        lnum = c

if a==b and a==c:
    print("All numbers are equal")
else:
    print("The largest number among",a,",",b,"and",c,"is: ",lnum)
