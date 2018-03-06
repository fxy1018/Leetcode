'''
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?

#method1: use hash to record node
#method2: fast and slow pointer
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        p1 = p2 = head
        
        while p1 and p2 :
            p1 = p1.next
            if p2.next:
                p2 = p2.next.next
            else:
                return(False)
            if p1 == p2:
                return(True)
        return(False)
