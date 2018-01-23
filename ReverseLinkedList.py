'''
Created on Jan 19, 2018

@author: XFan

LC: 
206. Reverse Linked List
92. Reverse Linked List II

'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #recursive
        return(self.helpFun(head, None))
    def helpFun(self, head, pre):
        if not head:
            return(pre)
        newHead = head.next
        head.next= pre
        return(self.helpFun(newHead, head))
    
    def reverseList2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #iteratively
        if not head:
            return(head)
        
        curr = head
        pre = None
        while curr:
            tmp = curr.next
            curr.next= pre
            pre = curr
            curr = tmp
        return(pre)
    
    
    
    
