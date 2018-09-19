"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root
    @return: minimum sum
    """
    def minimumSum(self, root):
        # Write your code here
        self.minSum = float("Inf")
        self.dfs(root, 0)
        return(self.minSum)
    
    def dfs(self, root, currSum):
        if not root.left and not root.right:
            self.minSum = min(self.minSum, currSum+root.val)
            return
        newcurrSum = currSum + root.val
        if root.left:
            self.dfs(root.left, newcurrSum)
        if root.right:
            self.dfs(root.right, newcurrSum)
        return
