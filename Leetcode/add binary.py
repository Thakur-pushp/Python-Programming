a = '11'
b = '1'

i = len(a)-1
j = len(b)-1
carry = 0
res = ''
while i >= 0 or j >= 0 or carry == 1:
    sum = carry

    if i >= 0:
        sum += int(a[i])
        i -= 1

    if j >= 0:
        sum += int(b[j])
        j -= 1

    
    carry = sum // 2
    res = str(sum%2) + res

print(res)
