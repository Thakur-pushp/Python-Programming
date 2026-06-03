nums1 = [2,6,2,9,1]
nums2 = [7,1]
# result = []
# smaller = nums1 if len(nums1)<len(nums2) else nums2
# larger = nums1 if smaller != nums1 else nums2
# for i in smaller:
#     if i in larger and i not in result:
#         result += [i]

# print(result)

n1 = set(nums1)
n2 = set (nums2)
res = n1.intersection(n2)
print(list(res))