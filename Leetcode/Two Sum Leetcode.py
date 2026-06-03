class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sum = []
        for i in range(0,len(nums),1):
            for j in range(0,len(nums),1):
                if i != j:
                    if nums[i] + nums[j] == target:
                        sum=[j,i]
        return sum   

nums = [4,5,7,9]
target = 13
obj = Solution()
a = obj.twoSum(nums, target)
print(a)
