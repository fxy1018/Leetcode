"""

Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].

Note: Recursive solution is trivial, could you do it iteratively?

"""

'''
Created on Mar 12, 2017

@author: fanxueyi
'''

#method1: Recursives solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = []
        self.helpFun(root)
        return(self.res)
        
    def helpFun(self, root):
        if not root:
            return
        self.helpFun(root.left)
        self.helpFun(root.right)
        self.res.append(root.val)

    #method2: two stack
    def postorderTraversal2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
            
        stack1 = [root]
        stack2 = []
        
        while stack1:
            curr = stack1.pop()
            stack2.append(curr)
            left = curr.left
            if left:
                stack1.append(left)
             
            right = curr.right
            if right:
                stack1.append(right)
        
        res = []
        while stack2:
            res.append(stack2.pop().val)
        return(res)
    
    
    #method3: one stack
    def postorderTraversal3(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []   
        stack = [root]
        curr = pre = root
        while stack:
            curr = stack[-1]
            if curr.left and pre != curr.left and pre!= curr.right:
                stack.append(curr.left)
            elif curr.right and pre!= curr.right:
                stack.append(curr.right)
            else:
                res.append(stack.pop().val)
                pre = curr
        return(res)
    
    #method4: morris travesal
        #method3: one stack
    def postorderTraversal3(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = []
        if not root:
            return []
        curr  = root
        while curr:
            temp = curr.left
            if temp:
                while temp.right and temp.right != curr:
                    temp = temp.right
                if temp.right == None:
                    temp.right = curr
                    curr = curr.left
                else:
                    temp.right = None
                    self.getTreeNodes(curr.left)
                    curr = curr.right
            else:
                curr = curr.right
        self.getTreeNodes(root)
        return(self.res)
        
    def getTreeNodes(self, node):
        tail = self.reverseEdge(node)
        curr = tail
        while curr:
            self.res.append(curr.val)
            curr = curr.right
        self.reverseEdge(tail)
    
    def reverseEdge(self, node):
        pre = next = None 
        while node:
            next = node.right
            node.right = pre
            pre = node
            node = next
        return pre
        
            
            
        