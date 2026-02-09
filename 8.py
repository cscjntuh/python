a = list(map(int, input("Enter first array: ").split()))
b = list(map(int, input("Enter second array: ").split()))

common = []

for i in a:
    if i in b and i not in common:
        common.append(i)

print("Common elements:", common)
