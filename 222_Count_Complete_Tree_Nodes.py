"""

Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

"""

'''
Created on Mar 12, 2017

@author: fanxueyi
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return(0)
            
        return self.bs(root, 1, self.mostLeftLevel(root, 1))
        
        
    def bs(self, node, l, h):
        if l == h:
            return 1
        if (self.mostLeftLevel(node.right, l+1) == h):
            return (2**(h-l) - 1 + 1 + self.bs(node.right, l+1, h))
        else:
            return (2**(h-l-1) -1 +1 + self.bs(node.left, l+1, h))
        
        
        
        
    def mostLeftLevel(self, node, level):
        while node:
            level += 1
            node = node.left
        return level-1
            
            
        
            
        
        
        
        
        
        
        
        