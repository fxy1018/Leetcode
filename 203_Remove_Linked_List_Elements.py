'''
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        out = dummy = ListNode(-1)
        while head:
            if head.val != val:
                dummy.next = ListNode(head.val)
                dummy = dummy.next
            head = head.next
        return(out.next)
        
   def removeElements2(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
       
        
        pre = dummy = ListNode(-1)
        pre.next = head
        
        while head:
            if head.val ==val:
                pre.next = head.next
            else:
                pre = pre.next
            head = head.next
            
        return(dummy.next)
