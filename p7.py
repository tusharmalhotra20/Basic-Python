principle = input("Enter principle amount:\t")
rate = input("Enter rate:\t")
time = input("Enter time:\t")

si = float(principle) * float(rate) * int(time) / 100

print("The simple interest is:\t", si)
