nums = [2,3,2,3]
val = 3
temp = []
for i in nums:
    if i != val:
        temp += [i]
nums [:]= temp
k = len(nums)
print(k,nums)