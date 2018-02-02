'''

Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

Note: The length of path between two nodes is represented by the number of edges between them.

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output:

2
Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output:

2
Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.

收集信息题目, postorder, 需要处理左右subtree传递来的信息

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return(0)
        
        self.res = 0
        self.getMax(root)
        return(self.res-1)
    
    def getMax(self, root):
        if not root:
            return(0)
        
        leftLen = self.getMax(root.left)
        rightLen = self.getMax(root.right)
        
        if root.left and root.val == root.left.val:
            leftLen = leftLen 
        else:
            leftLen = 0 
            
        if root.right and root.val == root.right.val:
            rightLen = rightLen 
        else:
            rightLen = 0 
            
        self.res = max(self.res, leftLen + rightLen + 1)
        
        return(max(leftLen, rightLen) + 1)
