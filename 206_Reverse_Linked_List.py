'''
Reverse a singly linked list.

click to show more hints.

Hint:
A linked list can be reversed either iteratively or recursively. Could you implement both?

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
        #iteratively
        
        if not head:
            return(head)
        
        tail = head 
        curr = head.next
        tail.next = None
        while curr:
            node = curr
            curr = curr.next
            node.next = tail
            tail = node
        return(tail)
    def reverseList2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #iteratively
        
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return(prev)
        
    def reverseList3(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #recursively
        
        return(self.helpFun(head, None))
        
    def helpFun(self, head, prev):
        if not head:
            return(prev)
        n = head.next
        head.next = prev
        return(self.helpFun(n, head))  
   
            
            
