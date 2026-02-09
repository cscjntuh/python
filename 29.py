f = open("file.txt")
word = input("Enter word to search: ")

if word in f.read():
    print("Word found")
else:
    print("Word not found")

f.close()
