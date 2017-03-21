"""

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:
    2
   / \
  1   3
Binary tree [2,1,3], return true.
Example 2:
    1
   / \
  2   3
Binary tree [1,2,3], return false.


"""

'''
Created on Feb 16, 2017

@author: fanxueyi
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.arr = []
    def isValidBST1(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #in-order traversal, recursively, but some code is unnecessary. 
        if not root:
            return(True)
        
        self.dfs(root)
        for i in range(1,len(self.arr)):
            if self.arr[i-1] >= self.arr[i]:
                return False
        return True
        
        
    def dfs(self, node):
        if not node.left and not node.right:
            self.arr.append(node.val)
            return
            
        if node.left:
            self.dfs(node.left)
            
        self.arr.append(node.val)
        
        if node.right:
           self.dfs(node.right)
           
    def isValidBST2(self, root):
            """
            :type root: TreeNode
            :rtype: bool
            """
             
            #in-order traversal, iteratively. 
            if not root:
                return(True)
            
            stack = []
            preval = -float("Inf")
            current = root
            done = False
            while not done:
                if current:
                    stack.append(current)
                    current = current.left
                else:
                    if(len(stack) >0 ):
                        current = stack.pop()
                        if current.val <= preval:
                            return(False)
                        preval = current.val
                 
                        # We have visited the node and its left 
                        # subtree. Now, it's right subtree's turn
                        current = current.right 
    
                    else:
                        done = True
            return True
    
    
    def isValidBST3(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
         
        #method1: in-order
        self.nodesArr = []
        self.inOrder(root)
        copyArr= self.nodesArr[:]
        self.nodesArr = sorted(set(self.nodesArr))
        return(copyArr == self.nodesArr)
        
        
    def inOrder(self, node):
        if not node:
            return()
        self.inOrder(node.left)
        self.nodesArr.append(node.val)
        self.inOrder(node.right)
                    

root = TreeNode(2)
root.left  = TreeNode(1)
root.right = TreeNode(3)

s = Solution()
s.isValidBST3(root) 