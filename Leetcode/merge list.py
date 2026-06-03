nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
temp = []
for i in range(m):
    temp += [nums1[i]]

for j in range(n):
        temp += [nums2[j]]
temp.sort()
nums1 [:]= temp
print(nums1)