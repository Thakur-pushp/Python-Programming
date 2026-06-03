s = "leetcode"
temp = {}
rep = set()
for i in range(len(s)):
    if s[i] not in temp and s[i] not in rep:
        temp[s[i]]=i 
    else:
        rep.add(s[i])
        if s[i] in temp:
            temp.pop(s[i])
t = list(temp)
res = s.index(t[0]) if t else -1
print(res)


