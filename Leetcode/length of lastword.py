class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # st = s.strip()
        temp = 0
        length = 0
        for i in s:
            if i != ' ':
                temp +=1
                length = temp
            else:
                temp = 0

        return(length)

s = "luffy is still joyboy            "
obj = Solution()
a = obj.lengthOfLastWord(s)
print(a)