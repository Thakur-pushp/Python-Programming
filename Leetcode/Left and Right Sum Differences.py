nums = [10,4,8,3]
leftsum = [0]
rightsum = [0]
result = []
for i in range(len(nums)-1):
    leftsum.append(leftsum[i]+nums[i])
for j in range(len(nums)-1,0,-1):
    rightsum.append(rightsum[-1]+nums[j])
rightsum = rightsum[::-1]
for k in range(len(nums)):
    result.append(abs(leftsum[k]-rightsum[k]))
# print(leftsum)
# print(rightsum)
print(result)