"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

"""

'''
Created on Jan 15, 2017

@author: fanxueyi
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    #method1: change linked-list to array
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return(None)
        changeArray = []
        while head:
            changeArray.append(head.val)
            head = head.next
        return(self.helpFun(changeArray))
        
    def helpFun(self, nums):
        
        if not nums:
            return(None)
        mid = len(nums)//2
        
        root = TreeNode(nums[mid])
        root.right = self.helpFun(nums[mid+1:])
        root.left = self.helpFun(nums[:mid])
    
        return(root)
    
    
    #method2: dealing with linkek-list directly
    def sortedListToBST2(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return(None)
        if not head.next:
            return(TreeNode(head.val))
            
        slow, fast = head, head.next.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None
        root = TreeNode(mid.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        
        return(root)
        
        
        
        
