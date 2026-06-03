s = ["h","e","l","l","o"]
m = len(s)
for i in range(0,m-1):
    s.insert(i,s[-1])
    s.pop()
print(s)