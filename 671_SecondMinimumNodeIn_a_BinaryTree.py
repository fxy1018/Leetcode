'''

Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:
Input: 
    2
   / \
  2   5
     / \
    5   7

Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.
Example 2:
Input: 
    2
   / \
  2   2

Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root or not root.left:
            return(-1)
        
        min1 = root.val
        min2 = -1
        
        stack  = [root]
        while stack:
            node = stack.pop()
            if node.val != min1 and min2 == -1:
                min2 = node.val
            elif node.val != min1 and min2!= -1:
                min2 = min(node.val, min2)
            else: #cut the subtree because node is the smallest one of the subtree
                if node.left:
                    stack.append(node.left)
                    stack.append(node.right)
        return(min2)
