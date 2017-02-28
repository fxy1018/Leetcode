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
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        postorder = postorder[::-1]
        return(self.helpFun(postorder, inorder, 0, len(postorder)-1, 0, len(inorder)-1))
    
    def helpFun(self, postorder, inorder, lp, rp, li, ri):
        if (lp >= rp):
            return(None)
        print(lp, rp, li, ri)
        root = TreeNode(postorder[lp])
        k = inorder.index(root.val)
        print(k)
        root.right = self.helpFun(postorder, inorder, lp+1, lp+(k-li),k+1, ri)
        root.left = self.helpFun(postorder, inorder, lp+(k-li)+1, rp, li, k-1)
        
        return(root)
    
    
    def buildTree2(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            index = inorder.index(postorder.pop())
            root = TreeNode(inorder[index])
            root.right = self.buildTree(inorder[index+1:], postorder)
            root.left = self.buildTree(inorder[:index], postorder)
            return root
    
    
 
s= Solution()
print(s.buildTree([2,1], [2,1]))
           