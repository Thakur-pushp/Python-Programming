nums = [0,0,1]
# last = len(nums)
# for i in range(last):
#     if nums[i] == 0:
#         nums.insert(last,0)
#         nums.remove(0)

# print(nums)
temp = []
count = 0
for i in range(len(nums)):
    if nums[i] != 0:
        temp += [nums[i]]
    else:
        count += 1
for j in range(count):
    temp += [0]
nums [::] = temp
print(nums)