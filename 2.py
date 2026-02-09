p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
n = int(input("Enter number of periods: "))

amount = p * (1 + r / 100) ** n
ci = amount - p

print("Compound Interest:", ci)
