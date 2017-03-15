"""

You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it exists.

Example:
Input: "4(2(3)(1))(6(5))"
Output: return the tree root node representing the following tree:

       4
     /   \
    2     6
   / \   / 
  3   1 5   
Note:
There will only be '(', ')', '-' and '0' ~ '9' in the input string.
An empty tree is represented by "" instead of "()".

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

#use stack to track the tree region
class Solution(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        if s == "":
            return(None)
        return(self.helpFun(s))
        
    def helpFun(self, s):
        if not s:
            return(None)
            
        i = 0
        nodeVal = ""
        while i< len(s) and s[i] != "(":
            nodeVal += s[i]
            i += 1
        
        node = TreeNode(int(nodeVal))
        leftS, rightS = self.getS(s[i:])
        
        
        leftNode = self.helpFun(leftS)
        rightNode = self.helpFun(rightS)
        node.left = leftNode
        node.right = rightNode
        return(node)
        
    def getS(self,s):
        if len(s) == 0:
            return(None, None)
        
        stack = [s[0]]
        leftS = []
        rightS= []
        p = 1
        while stack:
            if s[p] == ")":
                while stack[-1] != "(":
                    stack.pop()
                stack.pop()
            else:
                stack.append(s[p])     
            p += 1
        
        leftS = s[1:p-1]
       
        rightS = s[p+1:-1]
        return(leftS, rightS)
    

#use string find function
class Solution(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        index = s.find("(")
        if index < 0:
            return(TreeNode(int(s)) if s else None)
        pBalance = 0
#         for i in range(len(s)):
#             if s[i] == "(":
#                 pBalance += 1
#             if s[i] == ")":
#                 pBalance -= 1
#             if pBalance == 0 and index < i:
#                 breakIndex = i
#                 break
            
        #modified using enumerate
        for i, char in enumerate(s):
            if char == "(":
                pBalance += 1
            if char == ")":
                pBalance -= 1
            if pBalance == 0 and index < i:
                breakIndex = i
                break

    
        node = TreeNode(int(s[:index]))
        leftS, rightS = s[index+1 :breakIndex], s[breakIndex+2:-1]
        
        leftNode = self.str2tree(leftS)
        rightNode = self.str2tree(rightS)
        node.left = leftNode
        node.right = rightNode
        return(node)





        
s = Solution()
s.str2tree("4(2(3)(1))(6(5))")         
        
        
        
        
