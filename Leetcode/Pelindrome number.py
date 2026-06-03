class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        n = x
        num = 0
        while x> 0:
            digit = x % 10             
            num = (num * 10) + digit  
            x = x // 10
        if n == num:
            return "its pelindrome"
        else:
            return "it's not pelindrome"


x = 151
obj = Solution()
a = obj.isPalindrome(x)
print(a)