char = input("Enter a character: ")

if '0' <= char <= '9':
    print("Digit")
elif 'a' <= char <= 'z':
    print("Lowercase character")
elif 'A' <= char <= 'Z':
    print("Uppercase character")
else:
    print("Special character")
