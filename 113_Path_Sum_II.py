"""

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]

"""




'''
Created on Feb 12, 2017

@author: fanxueyi
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.path = []
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return(self.path)
        self.sum = sum
        currpath = []
        self.dfs(root, sum, currpath)
        return(self.path)
        
    def dfs(self, node, currsum, currpath):
        new_sum = currsum - node.val
        new_path = currpath + [node.val]
        if node.left == None and node.right == None:
            if new_sum == 0:
                self.path.append(new_path)
            return
        if node.left:
            self.dfs(node.left, new_sum, new_path)
        if node.right:
            self.dfs(node.right, new_sum, new_path)
 

#pre order travesal recursively
class Solution2(object):
    def pathSum(self, root, s):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return([])
        out = []
        stack = [[root, [root.val]]]
        while stack:
            node, ls = stack.pop()

            if not node.left and not node.right and sum(ls) == s:
                out.append(ls)
            
            if node.right:
                stack.append([node.right, ls+[node.right.val]])
            if node.left:
                stack.append([node.left, ls+[node.left.val]])
        return(out)
                
