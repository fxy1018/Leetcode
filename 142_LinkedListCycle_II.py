'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?

'''

#method1: Hash

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nodeHash = set([])
        
        while head:
            if head not in nodeHash:
                nodeHash.add(head)
                head = head.next
            else:
                return(head)
        return(None)
        

#mehtod2: two pointers

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution2(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p1 = p2 = head
        
        while p1 and p1.next:
            p1 = p1.next.next
            p2 = p2.next
            if p1 == p2:
                break
        if not p1 or not p1.next:
            return(None)
        
        p1 = head
        while p1!=p2:
            p1 = p1.next
            p2 = p2.next
        return(p1)
