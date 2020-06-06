#WAP to print smallest of three numbers using nested else-if.

a = float(input("Enter first number:\t"))
b = float(input("Enter second number:\t"))
c = float(input("Enter third number:\t"))

if a<b:
    if a<c:
        print("First number is lowest:\t", a)
    else:
        print("Third number is lowest:\t", c)
if b<a:
    if b<c:
        print("Second number is lowest:\t", b)
    else:
        print("Third number is lowest:\t", c)

if a==b and b==c:
    print("All numbers are equal")
