#Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

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
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #assume the l1 and l2 are asceding and require asceding output list
        if not l1 and not l2:
            return(None)
            
        out = ListNode(-1)
        head = out
        
        while l1 or l2:
            if not l1:
                while l2:
                    out.next = l2
                    out = out.next
                    l2 = l2.next
                    
            elif not l2:
                while l1:
                    out.next = l1
                    out = out.next
                    l1 = l1.next
                    
            elif l1.val < l2.val:
                out.next = l1
                out = out.next
                l1 = l1.next
                
            elif l2.val <= l1.val:
                out.next = l2
                out = out.next
                l2= l2.next
                
        return(head.next)
                
     
     # iteratively
def mergeTwoLists1(self, l1, l2):
    dummy = cur = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next
    
# recursively    
def mergeTwoLists2(self, l1, l2):
    if not l1 or not l2:
        return l1 or l2
    if l1.val < l2.val:
        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = self.mergeTwoLists(l1, l2.next)
        return l2
        
# in-place, iteratively        
def mergeTwoLists(self, l1, l2):
    if None in (l1, l2):
        return l1 or l2
    dummy = cur = ListNode(0)
    dummy.next = l1
    while l1 and l2:
        if l1.val < l2.val:
            l1 = l1.next
        else:
            nxt = cur.next
            cur.next = l2
            tmp = l2.next
            l2.next = nxt
            l2 = tmp
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next           
 
  # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = head = ListNode(-1)
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
                
            head = head.next
        if l1:
            head.next = l1
        if l2:
            head.next = l2
        return(res.next)  
    
  
