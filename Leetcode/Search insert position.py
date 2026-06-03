nums = [1,3,5,6]
target = 2

if target in nums:
    for i in range(len(nums)):
        if nums[i] == target:
            b = i
    print(b)
else:
    if nums[len(nums)-1]>target:
        for i in range(len(nums)):
            if nums[i] > target:
                b = i
                break
    else:
        b = len(nums)
    
    print(b)