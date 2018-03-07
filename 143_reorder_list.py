"""



"""

'''
Created on Mar 16, 2017

@author: fanxueyi
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        
        p1 = head
        p2 = head
        
        while p2 and p2.next:
            p2 = p2.next.next
            p1 = p1.next
          
         
        head2 = self.reverseList(p1.next)
        p1.next = None
        p = head
        while head2:
            nextP = p.next
            p.next = head2
            nextHead2 = head2.next
            head2.next = nextP
            p = nextP
            head2 =nextHead2
        
    def printList(self,head):
        while head:
            print(head.val)
            head = head.next
            
    def reverseList(self, node):
        pre = None
        next = None
        while node:
            next = node.next
            node.next = pre
            pre= node
            node = next
        return(pre)
 
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        
        p1 = p2 = head
        while p1 and p1.next:
            p1 = p1.next.next
            p2 = p2.next
            
        node = self.reverseList(p2.next)
        p2.next = None
        p3 = head
        while node:
            tmp = p3.next
            tmp2 = node.next
            p3.next = node
            node.next = tmp
            p3 = tmp
            node = tmp2
        
    def reverseList(self, node):
        pre = None
        curr = node
        while curr:
            tmp = curr.next
            curr.next = pre
            pre = curr
            curr = tmp
        return(pre)
            
        
node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)

s= Solution()
s.reorderList(node)   
        
