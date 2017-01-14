"""

Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.

"""


'''
Created on Jan 14, 2017

@author: fanxueyi
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return(None)
      
        p1 = p2 = head
        
        for i in range(n):
            p2 = p2.next
            
        if not p2:
            return(head.next)
        
        while p2.next:
            p1 = p1.next
            p2 = p2.next
        
        p1.next = p1.next.next   
        
        return(head)
        