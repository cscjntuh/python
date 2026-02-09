def is_sorted(lst):
    return lst == sorted(lst)

lst = list(map(int, input("Enter list elements: ").split()))

if is_sorted(lst):
    print("List is sorted")
else:
    print("List is not sorted")
