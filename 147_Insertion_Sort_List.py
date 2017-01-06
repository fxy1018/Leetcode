#Sort a linked list using insertion sort.

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
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return(head)
        
        dummy = ListNode(-1)
        dummy.next = pre = head
        point = head.next
        
        while point:
            q = dummy
            next = point.next
            if point.val < pre.val:
                while q.next and q.next!= point:
                    if q.next.val >=point.val:
                        pre.next =point.next
                        q.next, point.next = point, q.next
                        break
                    else:
                        q = q.next
            else:
                pre = point
            
            point = next
                    
        return(dummy.next)
            
            
            
    
                
                
            
            
        
