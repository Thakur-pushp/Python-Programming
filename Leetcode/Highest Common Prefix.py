class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # HCP will store
        prefix = ''

        # Shortest Element of list will store
        shortest = strs[0]

        # Finding Shortest Element
        for s in strs:
            if len(s)<len(shortest):
                shortest = s

        for j in range(len(shortest)):
            matchfound= True
            for k in strs:
                if shortest[j] != k[j]:
                        matchfound = False
                        break
            if matchfound:
                prefix+=(shortest[j])   
                
        # Final Printing
        return(prefix)


strs = ["cir","car"]
obj = Solution()
n = obj.longestCommonPrefix(strs)
print(n)