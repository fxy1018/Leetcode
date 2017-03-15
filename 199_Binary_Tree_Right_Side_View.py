"""

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4].



"""



'''
Created on Mar 13, 2017

@author: fanxueyi
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    #BFS+queue+Recursive
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return([])
            
        queue = [(root,0)]
        result = []
        while queue:
            node, level = queue.pop(0)
            if len(result) < level + 1:
                result.append(node.val)
            else:
                result[level] = node.val
            
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
        
        return(result)
    
#dfs recursive
class Solution2(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.dfs(root, 0, res)
        return(res)
    
    def dfs(self, root, depth, res):
        if not root:
            return
        
        if len(res) == depth:
            res.append(root.val)
            
        self.dfs(root.right, depth+1, res)
        self.dfs(root.left, depth+1, res)
        
#dfs iterative
class Solution3(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return([])
        res = []
        stack = [(root, 0)]
        while stack:
            node, level = stack.pop()
            if len(res) == level:
                res.append(node.val)
            
            if node.left:
                stack.append((node.left, level+1))
            if node.right:
                stack.append((node.right, level+1))
                
        return(res)     
        
        
