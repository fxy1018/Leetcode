"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

"""

'''
Created on Jan 15, 2017

@author: fanxueyi
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        #method 1: use stack, dfs
        if not root:
            return(False)
        stack = [(root, root.val)]
        while stack:
            curr, val = stack.pop()
            #check whether the node is leaf
            if not curr.left and not curr.right and val == sum:
                return(True)
            if curr.right:
                stack.append((curr.right, val+curr.right.val))
            
            if curr.left:
                stack.append((curr.left, val+curr.left.val))
            
        return(False)
            
            
        #method2: dfs recursively
        if not root:
            return(False)
        
        if not root.left and not root.right and root.val == sum:
            return(True)
        
        sum -=root.val
        
        return(self.hasPathSum(root.left,sum) or self.hasPathSum(root.right, sum))
            
        