'''
You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it exists.

 Notice
There will only be '(', ')', '-' and '0' ~ '9' in the input string.
An empty tree is represented by "" instead of "()".

Example
Given s = "4(2(3)(1))(6(5))", return the tree root node representing the following tree:

       4
     /   \
    2     6
   / \   / 
  3   1 5   

'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param s: a string
    @return: a root of this tree
    """
    def str2tree(self, s):
        # write your code here
        if not s:
            return(None)
            
        i = 0
        val = ""
        while i < len(s) and s[i] in "-1234567890":
            val += s[i]
            i += 1
     
        root = TreeNode(int(val))
        
        if i == len(s):
            leftS = rightS = None
        else:
            leftS, rightS = self._getSubTree(s[i:])

        root.left = self.str2tree(leftS)
        root.right = self.str2tree(rightS)
        
        return(root)
    
    def _getSubTree(self, s):
        if not s:
            return(None)
        subS = ""
        count = 0
        leftS = ""
        rightS = ""
        for i in range(0, len(s)):
            if s[i] == "(":
                count += 1
            if s[i] == ")":
                count -= 1
            subS+=s[i]
            
            if count == 0:
                if leftS == "":
                    leftS = subS
                    subS = ""
                else:
                    rightS = subS

        
        if len(leftS) > 0:
            leftS = leftS[1:len(leftS)-1]
        if len(rightS) > 0:
            rightS = rightS[1:len(rightS)-1]
        
        return(leftS, rightS)
            
