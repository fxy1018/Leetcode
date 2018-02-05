'''

Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
Input:

    2
   / \
  1   3

Output:
1
Example 2: 
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
Note: You may assume the tree (i.e., the given root node) is not NULL.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return(None)
        
        queue=[(root, 1)]
        res = []
        p = 0
        while queue: 
            node, level = queue[0]
            queue = queue[1:]
            if node.left:
                queue.append((node.left,level+1))
            
            if node.right:
                queue.append((node.right,level+1))
            if len(res) < level:
                res.append([node.val])
            else:
                res[level-1].append(node.val)
        return(res[-1][0])
