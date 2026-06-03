nums1 = '11'
nums2 = '123'
sum1 = 0
sum2 = 0
for i in range(len(nums2)):
    digits = (ord(nums2[i])-48)
    sum1 = (sum1*10)+digits


for j in range(len(nums1)):
    digits = (ord(nums1[j])-48)
    sum2 = (sum2*10)+digits

print(str(sum1 + sum2))