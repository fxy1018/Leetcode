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

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution2:
   #time:O(n), space: O(n)
   def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #pre order
        if not root:
            return([])
        dic = {}
        stack = [root]
        while stack:
            root = stack.pop()
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
            dic[root.val] = dic.get(root.val, 0) + 1
        
        out = []
        count = 0
        for key in dic:
            if dic[key] > count:
                out = []
                out.append(key)
                count = dic[key]
            elif dic[key] == count:
                out.append(key)
        return(out)   
   
   def findMode2(self.root):
      
   #Morris travesal in order: time: O(N), space: O(1)
   # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        self.modes = []
        self.modesCount = 0
        self.currCount = 0
        self.preValue = -float("Inf")
        self.morrisInOrder(root)
        return(self.modes)
        
        
    def morrisInOrder(self,root):
        if not root:
            return([])
        out = [(None, 0)]
        count = 0
        while root:
            if root.left:
                tmp = root.left
                while tmp.right and tmp.right != root:
                    tmp = tmp.right
                if not tmp.right:
                    tmp.right = root
                    root = root.left
                    
                elif tmp.right == root:
                    self.handleValue(root.val)
                    tmp.right = None
                    root = root.right   
            else:
                self.handleValue(root.val)
                root = root.right
    
    def handleValue(self, val):
        if val != self.preValue:
            self.preValue = val
            self.currCount = 1
        else:
            self.currCount += 1
            
        if self.currCount > self.modesCount:
            self.modesCount = self.currCount
            self.modes = [val]
        elif self.currCount == self.modesCount:
            self.modes.append(val)
        
    
      
  
root = TreeNode(1)
root.left = None
root.right = TreeNode(2)

s= Solution()
print(s.findMode(root))
 
