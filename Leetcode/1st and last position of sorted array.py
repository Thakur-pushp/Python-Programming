nums = [2,2]
target = 2
result = []    
starting = -1
ending = -1
if not target in nums:
    result += [starting,ending]
elif len(nums)<2:
    if target in nums:
        starting,ending = 0,0
        result += [starting,ending]
else:
    for i in range (len(nums)):
        if nums[i] == target and starting == -1:
            starting = i
        if nums[i] == target:
            ending = i
    result += [starting,ending]
print(result)







        
        