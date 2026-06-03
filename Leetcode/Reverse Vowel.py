s = "IceCreAm"
vowl = []
for i in s:
    if i.lower() in ['a','e','i','o','u']:
        vowl += [i]
sl = list(s)
for j in range(len(s)):
    if s[j].lower() in ['a','e','i','o','u']:
        sl[j] = vowl[len(vowl)-1]
        vowl.pop()
res = ''.join(sl)
print(res)