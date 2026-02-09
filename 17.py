s = input("Enter a sentence: ")
res = ""
cap = True

for ch in s:
    if ch == " ":
        cap = True
        res += ch
    else:
        if cap:
            res += ch.upper()
            cap = False
        else:
            res += ch.lower()

print("Result:", res)
