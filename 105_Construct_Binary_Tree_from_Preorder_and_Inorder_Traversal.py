"""

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

"""

'''
Created on Feb 27, 2017

@author: fanxueyi
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return(self.helpFun(preorder, inorder, 0, len(preorder)-1, 0, len(inorder)-1))
    
    def helpFun(self, preorder, inorder, lp, rp, li, ri):
        if (lp > rp ):
            return(None)
        root = TreeNode(preorder[lp])
        k = inorder.index(root.val)
        root.left = self.helpFun(preorder, inorder, lp+1, lp+(k-li), li, k-1)
        root.right = self.helpFun(preorder, inorder, lp+(k-li)+1, rp, k+1, ri)
        
        return(root)
    
    #modified
    def buildTree2(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            index = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[index])
            root.left = self.buildTree(preorder, inorder[:index])
            root.right = self.buildTree(preorder, inorder[index+1:])
            return root
        
 #sceond time 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution2:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return(None)
        
        root = TreeNode(preorder[0])
        n = len(preorder)
      
        index = inorder.index(preorder[0])
        leftPreorder = preorder[1: 1+index]
        rightPreorder = preorder[1+index:]
        leftInorder = inorder[0:index]
        rightInorder= inorder[index+1:]
        
#         for i in range(n):
#             if preorder[0] == inorder[i]:
#                 leftPreorder = preorder[1: 1+i]
#                 rightPreorder = preorder[1+i:]
#                 leftInorder = inorder[0:i]
#                 rightInorder= inorder[i+1:]
                
        root.left = self.buildTree(leftPreorder, leftInorder)
        root.right = self.buildTree(rightPreorder, rightInorder)
        
        return(root)
            
        
            
