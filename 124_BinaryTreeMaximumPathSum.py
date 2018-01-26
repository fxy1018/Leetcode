'''
Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.


'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return(0)
        res, singleSum = self.postOrder(root, -float("Inf"), -float("Inf"))
        return(res)
    def postOrder(self, root, maxSum, singleSum):
        if not root:
            return(maxSum, singleSum)
        
        leftMaxSum, leftSingleSum = self.postOrder(root.left, maxSum, singleSum)
        rightMaxSum, rightSingleSum= self.postOrder(root.right, maxSum, singleSum)
        
        value = root.val
        #if path across node
        acrossSum = max(leftSingleSum,0) + value + max(rightSingleSum,0)
        #compare three situation, path across node, left maxSum path and right maxSum path
        currMaxSum = max(acrossSum, leftMaxSum, rightMaxSum)
        currSingleSum = max(leftSingleSum, rightSingleSum,0) + value
        return(currMaxSum, currSingleSum)
        
