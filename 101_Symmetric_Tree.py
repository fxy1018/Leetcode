###
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
###

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return(self.helpFun(root, root))
    def helpFun(self, right, left):
        if not right and not left:
            return(True)
        if (not right and left) or (right and not left):
            return(False)
        if right == left:
            return(self.helpFun(right.right, left.left))
        if right.val != left.val: 
            return(False)
        
        return(self.helpFun(right.right, left.left) and self.helpFun(right.left, left.right))
        


class Solution2(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: 
            return(True)
        
        queue_left = [root.left]
        queue_right = [root.right]
        
        while queue_left and queue_right:
            left_node = queue_left[0]
            right_node = queue_right[0]
            queue_left = queue_left[1:]
            queue_right = queue_right[1:]
            
            if not left_node and not right_node:
                continue
            
            if (not left_node and right_node) or (left_node and not right_node):
                return(False)
            
            if left_node.val != right_node.val :
                return(False)
            queue_left.append(left_node.left)
            queue_left.append(left_node.right)
            queue_right.append(right_node.right)
            queue_right.append(right_node.left)
            
        if queue_left or queue_right:
            return(False)
        return(True)
            
