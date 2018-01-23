'''
Created on Jan 19, 2018

@author: XFan

LC: 19

remove kth node from end of list (single and double)

'''
from _hashlib import new

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
        if not head or n < 1:
            return(head)
        curr = head
        while curr:
            curr = curr.next
            n -=1
        if n == 0:
            head = head.next
        if n < 0:
            curr = head
            n += 1
            while n <0:
                curr = curr.next
                n += 1
            curr.next = curr.next.next
        return(head)
    
    
    def removeNthFromEnd2(self, head, n): #double linked list
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head or n < 1:
            return(head)
        curr = head
        while curr:
            curr = curr.next
            n -=1
        if n == 0:
            head = head.next
            head.last = None
        if n < 0:
            curr = head
            n += 1
            while n <0:
                curr = curr.next
                n += 1
            new = curr.next.next
            curr.next = new
            if new:
                new.last = curr
        return(head)
        
        
        
