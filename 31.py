f = open("file.txt")
text = f.read()

print("Words:", len(text.split()))
print("Vowels:", sum(1 for c in text if c.lower() in "aeiou"))
print("Spaces:", text.count(" "))
print("Lowercase letters:", sum(1 for c in text if c.islower()))
print("Uppercase letters:", sum(1 for c in text if c.isupper()))

f.close()
