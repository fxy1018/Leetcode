
#Sort a linked list in O(n log n) time using constant space complexity.


'''
Created on Jan 5, 2017

@author: fanxueyi 
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode    
        :rtype: ListNode
        """
        #list is empty or only one element
        if not head or not head.next:
            return(head)
        #set two pointers
        slow = head
        fast = head.next
        
        #get the middle position
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #seperate list to two part
        p2 = slow.next
        slow.next = None
        
        left = self.sortList(head)
        right = self.sortList(p2)
        
        #merge list
        return(self.merge(left, right))
    
    def merge(self, l, r):
        """
        help funtion to merge two sorted linked list
        :type l/r: ListNode
        :rtype: ListNode
        
        """
        if not l or not r:
            return l or r
        
        # get the head which should be the left node with smaller value
        if l.val > r.val :
            l, r = r, l
        
        #head: return
        #pre: record previous position
        #
        head, pre = l, l 
        l = l.next
        
        while l and r:
            if l.val < r.val:
                pre.next = l
                l = l.next
            else:
                pre.next = r
                r = r.next
            pre = pre.next
            
        #the l or r: at least one is None
        pre.next = l or r
        return(head)
                            
    
        