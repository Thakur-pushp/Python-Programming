s = "A man, a plan, a canal: Panama"

a = ''.join(i.lower()for i in s if i.isalnum())
for i in s.lower():
    if ('a'<= i <= 'z') or ("0" <= i <= '9'):
        a += i
rev = a[::-1]
if rev == a:
    print(True)
else:
    print(False)