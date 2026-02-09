def remove_duplicates(lst):
    return list(set(lst))

lst = list(map(int, input("Enter list elements: ").split()))

print("List without duplicates:", remove_duplicates(lst))
