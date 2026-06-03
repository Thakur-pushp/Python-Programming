nums = [4,3,2,7,8,2,3,1]
temp = set(nums)
n = len(nums)
res = []
for i in range (1,n+1):
    if i not in temp:
        res += [i]
print(res)