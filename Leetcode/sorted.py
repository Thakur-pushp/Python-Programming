class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = []
        for i in nums:
            if i not in temp:
                temp = temp + [(i)]
        k = len(temp)
        nums [:]=temp
        return k,nums
        
    
nums = [1,1,2]
obj = Solution()
a = obj.removeDuplicates(nums)
print(a)