'''
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:
     3
    / \
   2   3
    \   \ 
     3   1
Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:
     3
    / \
   4   5
  / \   \ 
 1   3   1
Maximum amount of money the thief can rob = 4 + 5 = 9.

Strategy:
rob_root = max(rob_L + rob_R , no_rob_L + no_nob_R + root.val)
no_rob_root = rob_L + rob_R

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return(0)
        self.res = 0
        #postorder
        self.helpFun(root)
        return(self.res)
        
    def helpFun(self, node):
        if not node:
            return((0,0))
        leftRob, leftNoRob = self.helpFun(node.left)
        rightRob, rightNoRob = self.helpFun(node.right)
        
        rob = node.val + leftNoRob + rightNoRob
        noRob = leftRob + rightRob
        self.res = max(self.res, rob, noRob)
        return(max(rob,noRob), noRob)
