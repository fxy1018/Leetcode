'''

Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

Example
Examples 1
Input:

  5
 /  \
2   -3
return [2, -3, 4], since all the values happen only once, return all of them in any order.

Examples 2
Input:

  5
 /  \
2   -5
return [2], since 2 happens twice, however -5 only occur once.

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
    @param root: the root
    @return: all the values with the highest frequency in any order
    """
    def findFrequentTreeSum(self, root):
        # Write your code here
        sumHash = {}
        self.helpFun(root,sumHash)
        res = []
        frequency = 0
        for key in sumHash:
            if sumHash[key] > frequency:
                frequency = sumHash[key]
                res = [key]
            elif sumHash[key] == frequency:
                res.append(key)
        return(res)
    
    def helpFun(self, node, sumHash):
        if not node:
            return(0)
        
        left = self.helpFun(node.left, sumHash)
        right = self.helpFun(node.right, sumHash)
        
        currSum = left+right+node.val
        sumHash[currSum] = sumHash.get(currSum, 0) + 1
        
        return(currSum)
