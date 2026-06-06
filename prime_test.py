n = int(input())
# temp = []
count = 0
res = ''
for i in range(1,n+1):
    if n % i == 0:
        count += 1
    if count == 3:
        res = 'composite'
        break
    else:
        res = 'prime'
print(res)