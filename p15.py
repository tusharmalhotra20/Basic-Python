#WAP to print smallest of three numbers.

a = float(input("Enter first number:\t"))
b = float(input("Enter second number:\t"))
c = float(input("Enter third number:\t"))

if a<b and a<c:
    snum = a
elif b<a and b<c:
    snum = b
else:
    snum = c
print("The smallest number among ", a, ",", b, ", and", c, "is:\t", snum)
