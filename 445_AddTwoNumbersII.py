'''

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7

'''
#method1: reverse list to count result, no fast enough
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_r = self.reverseList(l1)
        l2_r = self.reverseList(l2)
        res = dummy= ListNode(-1)
        div = 0
        while l1_r or l2_r:
            addTwo = div
            if l1_r:
                addTwo += l1_r.val 
            if l2_r:
                addTwo += l2_r.val
                
            div, mod = divmod(addTwo, 10)
            dummy.next = ListNode(mod)
            dummy = dummy.next
            if l1_r:
                l1_r = l1_r.next
            if l2_r:
                l2_r = l2_r.next
        if div == 1:
            dummy.next = ListNode(div)
            
        return(self.reverseList(res.next))
        
        
    def reverseList(self, node):
        pre =None 
        curr = node
        while curr:
            tmp = curr.next
            curr.next =pre
            pre= curr
            curr =tmp
        return(pre)
        
