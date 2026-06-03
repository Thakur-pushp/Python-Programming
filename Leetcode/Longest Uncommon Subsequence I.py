a = "aefawfawfawfaw"
b = "aefawfeawfwafwaef"
for i in range(len(b)):
    if a == b:
        c = -1
        break
    else:
        c = len(a) if len(a)>len(b) else len(b)
print(c)