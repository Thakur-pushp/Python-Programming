class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res = True

        if len(s) % 2 != 0:
            print('a')
            res = False

        stack = []
        dic = {'(':')','{':'}','[':']'}

        
        for i in s:
            if i in dic:
                stack.append(i)
            else:
                if not stack or dic[stack[-1]] != i:
                    res = False
                    break
                else:
                    res = True
                    stack.pop()
        return(res)
    

s = "(("
obj = Solution()
a = obj.isValid(s)
print(a)