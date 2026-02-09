def has_duplicates(lst):
    return len(lst) != len(set(lst))

lst = list(map(int, input("Enter list elements: ").split()))

if has_duplicates(lst):
    print("Duplicates found")
else:
    print("No duplicates")
