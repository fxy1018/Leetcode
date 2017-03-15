"""
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
For example:
Given BST [1,null,2,2],
   1
    \
     2
    /
   2
return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).


"""

'''
Created on Mar 14, 2017

@author: fanxueyi
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        dic = {}
        self.dfs(root, dic)
        res = []
        count = 0
        for key in dic:
            if dic[key] > count:
                res = [key]
                count = dic[key]
            elif dic[key] == count:
                res.append(key)
        return(res)
        
        
    def dfs(self, node, dic):
        if not node:
            return
        dic[node.val] = dic.get(node.val, 0) + 1
        self.dfs(node.left, dic)
        self.dfs(node.right, dic)

root = TreeNode(1)
root.left = None
root.right = TreeNode(2)

s= Solution()
print(s.findMode(root))
 