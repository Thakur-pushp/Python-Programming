# Input 
nums1 = [4,1,2]
nums2 = [1,3,4,2]

# result list
res =[]

# Loop in list nums1
for i in nums1:
    #Taking the first element of the list as the maximum element in nums2
    maz = i
    # loop starts from i_th elemnt in nums2 to last element of nums2
    for j in range(nums2.index(i),len(nums2)):
        # Checking if there's any greater element after i in nums2
        if maz < nums2[j]:
            maz = nums2[j]
            break
    # If there's no greater element then maximum value will be -1
    if maz == i:
        maz = -1
    # Store maximum value in resultant list
    res += [maz]

print(res)
