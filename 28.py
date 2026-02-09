f1 = open("file1.txt")
f2 = open("file2.txt")
f3 = open("file3.txt", "w")

f3.write(f1.read())
f3.write(f2.read())

f1.close()
f2.close()
f3.close()

print("Files merged successfully")
