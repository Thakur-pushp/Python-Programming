s = 'abcd'
t = 'dabec'
sum1 = 0
sum2 = 0

for i in s:
    sum1 += ord(i)

for j in t:
    sum2 += ord(j)

print(chr(sum2 - sum1))