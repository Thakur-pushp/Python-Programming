a = 'PuShp'
# print(a.isupper() or a.istitle() or a.islower())
count = 0
for i in a:
    b = ord(i)
    if b >= 65 and b <= 91:
        count += 1

if count == len(a) or count == 0:
    print(True)
elif count == 1 and a[0] >= chr(65) and a[0]<= chr(91):
    print(True)
else:
    print(False)
