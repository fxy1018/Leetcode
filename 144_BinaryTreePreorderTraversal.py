# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #recursively
        res = []
        self.preOrder(root, res)
        return(res)
    
    def preOrder(self, root, res):
        if not root:
            return
        
        res.append(root.val)
        self.preOrder(root.left, res)
        self.preOrder(root.right, res)
