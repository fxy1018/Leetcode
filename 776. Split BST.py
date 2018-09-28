# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def splitBST(self, root, V):
        """
        :type root: TreeNode
        :type V: int
        :rtype: List[TreeNode]
        """  
        if not root:
            return(None, None)
        if root.val <= V:
            res = self.splitBST(root.right, V)
            root.right = res[0]
            return(root, res[1])
        elif root.val > V:
            res = self.splitBST(root.left, V)
            root.left = res[1]
            return(res[0], root)
            
   
