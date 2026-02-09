f = open("file.txt")
words = f.read().split()

max_word = max(words, key=words.count)
print("Most repeated word:", max_word)

f.close()
