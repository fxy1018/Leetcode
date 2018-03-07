"""

Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 <= m <= n <= length of list.

"""
from macholib.mach_o import prebind_cksum_command

'''
Created on Feb 24, 2017

@author: fanxueyi
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m==n :
            return(head)
            
        dummy = ListNode(-1)
        dummy.next = head

        head = p1 = p2 = dummy
        

        for i in range(m-1):
            p1 = p1.next
        
        for j in range(n):
            p2 = p2.next
          
        for i in range(n-m):
            temp_node = p1.next
            p1.next= p1.next.next
            temp_node.next = p2.next
            p2.next = temp_node
            
        return(head.next)
    
    
    
    #modified the code        
    def reverseBetween2(self, head, m, n):
        if m==n :
            return(head)
        
        dummy = ListNode(-1)
        dummy.next = head
        head = dummy
        
        for i in range(m-1):
             head = head.next
        
        pre = head.next
        curr = pre.next
        
        for i in range(n-m):
            temp = curr.next
            curr.next = pre
            pre = curr
            curr = temp
        
        head.next.next = curr
        head.next = pre
        head = dummy.next
        return(head)
        
        
        
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        i = 1
        p1 = head
        pre = None
        while i < m:
            pre = p1
            p1= p1.next
            i += 1
    
        node = self.reverseList(p1, n-m)
        if pre:
            pre.next = node
            return(head)
        else:
            return(node)
        
    def reverseList(self, node, c):
        if c == 0:
            return(node)
        count = 0
        pre = None
        curr = node
        while count <= c:
            tmp = curr.next
            curr.next = pre
            pre = curr
            curr= tmp
            count += 1
        
        node.next = curr
        return(pre)
                



##############Test Part##################        
 
node1 = ListNode(3)
node2 = ListNode(5)
node3 = ListNode(7)
node4 = ListNode(9)
node1.next = node2
node2.next = node3
node3.next = node4
s= Solution()

def printNode(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(res)

printNode(s.reverseBetween(node1, 2, 3))      
