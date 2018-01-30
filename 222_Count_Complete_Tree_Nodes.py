"""

Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

"""

'''
Created on Mar 12, 2017

@author: fanxueyi
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Solution1(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #method1: BFS or DFS, time exceed, O(n)
        if not root:
            return(0)
        
        return(1+self.countNodes(root.left)+self.countNodes(root.right))

class Solution2(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return(0)
            
        return self.bs(root, 1, self.mostLeftLevel(root, 1))
        
        
    def bs(self, node, l, h):
        if l == h:
            return 1
        if (self.mostLeftLevel(node.right, l+1) == h):
            return (2**(h-l) - 1 + 1 + self.bs(node.right, l+1, h))
        else:
            return (2**(h-l-1) -1 +1 + self.bs(node.left, l+1, h))
        
        
        
        
    def mostLeftLevel(self, node, level):
        while node:
            level += 1
            node = node.left
        return level-1
            
            
        
            
        
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution3(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #method2: use the complete tree node 
        if not root:
            return(0)
        hight = self.getLeftMostLevel(root)
        return(self.helpFun(root, hight))
    
    def helpFun(self, node, hight):
        if hight == 0:
            return(0)
        
        rightHight = self.getLeftMostLevel(node.right)
        if hight == rightHight+1:
            return(2**(hight-1) + self.helpFun(node.right, rightHight))
        else:
            return(2**(hight-2) + self.helpFun(node.left, hight-1)) 

    
    def getLeftMostLevel(self, node):
        level = 1
        while node:
            level += 1
            node = node.left
        return(level-1)
        
        
        
        
