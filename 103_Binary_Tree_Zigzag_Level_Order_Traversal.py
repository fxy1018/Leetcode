"""

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return([])
        res = []
        queue = [(root,1)]
        self.bfs(res, queue)
        return(res)
        
        #use bfs to get result
    def bfs(self, res, queue):
        while queue:
            (currnode, depth) = queue.pop(0)
            if len(res) < depth:
                    res.append([currnode.val])
            else:
                if depth%2 == 1:
                    res[depth-1].append(currnode.val)
                if depth%2 == 0:
                    res[depth-1].insert(0, currnode.val)
            if currnode.left:
                queue.append((currnode.left, depth+1))
            if currnode.right:
                queue.append((currnode.right, depth+1))
            
            
    