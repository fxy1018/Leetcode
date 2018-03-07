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
            
            
            
    
                
                
     # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#create a dummy head and pre pointer
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
        node = head.next
        
        while node:
            q1 = dummy
            nextNode = node.next
            
            if node.val < pre.val:
                while q1.next and q1.next != node:
                    if q1.next.val>=node.val:
                        pre.next = nextNode
                        tmp = q1.next
                        q1.next = node
                        node.next = tmp
                        break
                    else:
                        q1 = q1.next
                    
            else:
                pre = node
            
            node = nextNode
                
        return(dummy.next)       
            
        
