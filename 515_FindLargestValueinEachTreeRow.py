'''
You need to find the largest value in each row of a binary tree.

Example:
Input: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [1, 3, 9]

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return([])
        
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
                res.append(node.val)
            else:
                res[level-1] = max(res[level-1], node.val)
        return(res)
