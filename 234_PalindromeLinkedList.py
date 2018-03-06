'''

Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?

'''

#method1: use stack
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        stack = []
        p = head
        while p:
            stack.append(p)
            p = p.next
        
        while head:
            top = stack.pop()
            if top.val == head.val:
                head = head.next
            else:
                return(False)
        return(True)

#method2: use half space stack
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        stack = []
        p1 = p2 = head
        while p1 and p1.next:
            p1 = p1.next.next
            p2 = p2.next
            
        while p2:
            stack.append(p2)
            p2 = p2.next
        
        while stack:
            top = stack.pop()
            if top.val == head.val:
                head = head.next
            else:
                return(False)
        return(True)
        
#method3: use two pointers and reverse linked list\
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        p1 = p2 = head
        while p1 and p1.next:
            p1 = p1.next.next
            p2 = p2.next
        end = self.reverseList(p2)
        dump = end
        while dump:
            if dump.val == head.val:
                dump = dump.next
                head = head.next
            else:
                self.reverseList(end)
                return(False)
        self.reverseList(end)
        return(True)
    
    def reverseList(self, head):
        pre = None
        curr = head
        while curr:
            tmp = curr.next
            curr.next = pre
            pre = curr
            curr = tmp
        return(pre)


