d = {}
n = int(input("Enter number of key-value pairs: "))

for i in range(n):
    k = input("Enter key: ")
    v = input("Enter value: ")
    d[k] = v

inv = {}

for k in d:
    inv[d[k]] = k

print("Inverted dictionary:", inv)
