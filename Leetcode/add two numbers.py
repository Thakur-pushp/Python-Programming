# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result =[]
        num1 = 0
        num2 = 0
        for i in range(len(l1)-1,-1,-1):
            num1 = (num1 * 10) + (l1[i])
        for j in range(len(l2)-1,-1,-1):
            num2 = (num2 * 10) + (l2[j])   
        num = num1 + num2
        while num>0:
            result += [(num % 10)]
            num = num // 10

        return(result)


l1 = [2,4,3]
l2 = [5,6,4]   
obj = Solution()
a = obj.addTwoNumbers(l1,l2)
print(a)