s = "anagram"
t = "nagaram"
res = True
a = []
a.extend(i for i in s)
if len(t) != len(s):
    res = False
else:
    for i in t:
        if i not in a:
            res = False
            break
        else:
            a.remove(i)
            res = True

print(res)
