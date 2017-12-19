'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
#method1: use two link list to store less and more nodes, O(n), space: O(n)
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return head
        
        p1 = more = ListNode(-1)
        p2 = less = ListNode(-1)
        
        while head:
            if head.val >= x:
                p1.next = ListNode(head.val)
                p1 = p1.next
            else:
                p2.next = ListNode(head.val)
                p2 = p2.next
                
            head = head.next
            
        p2.next = more.next
        return(less.next)
  
    def partition2(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return head
        
        p1 = more = ListNode(-1)
        p2 = less = ListNode(-1)
        
        while head:
            if head.val >= x:
                p1.next = head
                p1 = p1.next
            else:
                p2.next = head
                p2 = p2.next
                
            head = head.next
        
        p1.next = None
        p2.next = more.next
        return(less.next)
