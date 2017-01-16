"""

Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

"""

'''
Created on Jan 16, 2017

@author: fanxueyi
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head:
            return(head)
            
        dummy = ListNode(0)
        dummy.next =  head
        out = dummy
        
        while dummy.next and dummy.next.next:
            a = dummy.next
            b = a.next
            
            a.next = b.next
            b.next = a
            dummy.next = b
            
            #dummy.next, b.next, a.next =  b, a, b.next
            
            dummy = a
            
        return(out.next)
        
        
        
    
     
        