#WAP to calculate average marks of student and display grades according to it.

m1 = float(input("Enter marks for English:\t"))
m2 = float(input("Enter marks for Hindi:\t"))
m3 = float(input("Enter marks for Science:\t"))
m4 = float(input("Enter marks for Mathematics:\t"))
m5 = float(input("Enter marks for Social science:\t"))

t = (m1+m2+m3+m4+m5)/5

print("Percentage obtained:", t,"%")

if (t>=90) and (t<=100):
    print("Grade: A")
elif (t>=80) and (t<90):
    print("Grade: B")
elif (t>=70) and (t<80):
    print("Grade: C")
elif (t>=60) and (t<70):
    print("Grade: D")
elif (t>=50) and (t<60):
    print("Grade: E")
else:
    print("FAIL")
