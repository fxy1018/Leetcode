```

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

```

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        #bfs
        if not root:
            return([])
        queue = [(root, 1)]
        out = []
        while queue:
            node, level = queue.pop()
            if node.left: 
                queue.insert(0, (node.left, level + 1))
            if node.right:
                queue.insert(0, (node.right, level + 1))
            
            if len(out) < level:
                out.append([node.val])
            else:
                out[level-1].append(node.val)
                
        return(out)      
                
