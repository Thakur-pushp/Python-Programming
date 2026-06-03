nums = [2,1,2,3]
# a = set(nums)
# if len(a) > 2:
#     for i in range(2):
#         a.remove(max(a))
# print(max(a))
first = nums[0]
second = nums[0]
third = nums[0]
for i in nums:
    if i == first or i == second or i == third:
        continue
    elif i>first:
        third = second
        second = first
        first = i
    elif i > second:
        third , second = second , i
    else:
        third = i
print(third)