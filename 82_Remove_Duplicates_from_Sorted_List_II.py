'''
Created on Feb 1, 2017

@author: fanxueyi
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


#http://bangbingsyb.blogspot.com/2014/11/leetcode-remove-duplicates-from-sorted_19.html
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return(head)
        
        dummy = ListNode(-1)
        dummy.next= head
        pre = dummy
        curr = head
        duplicate = False
        while curr:
            if curr.next and curr.val == curr.next.val:
                temp = curr.next
                curr.next = temp.next
                duplicate = True
            elif duplicate:
                pre.next = curr.next
                curr= pre.next
                duplicate = False
            
            else:
                pre = curr
                curr = curr.next
        
        return(dummy.next)
                
                
            
        
        