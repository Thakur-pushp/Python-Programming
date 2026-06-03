a = [1]
k = 1
temp = {}
res = False
for i in range(len(a)):
    if a[i] in temp:
        if abs(temp[a[i]]-i) <= k:
            res = True
            break
        else:
            res = False
    temp[a[i]] = i
print(res)

