ransomNote = "aa"
magazine = "ab"
a,b = list(ransomNote),list(magazine)
result = True
for i in ransomNote:
    if i in b:
        b.remove(i)
        result = True
    else:
        result = False
        break
print(result)