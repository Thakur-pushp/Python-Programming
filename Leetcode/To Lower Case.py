s = "Hello@[]"
res = ''
for i in s:
    if ord(i) >= 65 and ord(i)<91:
        res += chr(ord(i)+32)
    else:
        res += i
print(res)
