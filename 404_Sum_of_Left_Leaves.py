'''
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return(0)
        
        return(self.helpFun(root, False, 0))
    
    def helpFun(self, root, isLeft, sum):
        if not root.left and not root.right and isLeft:
            return(sum + root.val)

        leftSum = 0
        rightSum = 0
        
        if root.left:
            leftSum = self.helpFun(root.left, True, sum)
        if root.right:
            rightSum = self.helpFun(root.right, False, sum)
            
        return(leftSum + rightSum)
    
    
    #modified
    
    def sumOfLeftLeaves2(self, root):
        if not root:
            return(0)
        if root.left and not root.left.left and not root.left.right:
            return(root.left.val + self.sumOfLeftLeaves2(root.right)
        return(self.sumOfLeftLeaves2(root.left) + self.sumOfLeftLeaves(root.right))

    
    
