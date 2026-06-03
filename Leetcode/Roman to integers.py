class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.upper()
        roman=['I','V','X','L','C','D','M']
        length = len(s)
        symbols = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        if length<=1:
            return (symbols[s])
        else:
            total = 0
            for i in range(0,length-1,1):
                if symbols[s[i]]<symbols[s[i+1]]:
                    total -= (symbols[s[i]])
                    i += 1
                else:
                    total += symbols[s[i]]
            total += symbols[s[-1]]
            return(total)



s = "LVIII"
obj = Solution()
a = obj.romanToInt(s)
print (a)