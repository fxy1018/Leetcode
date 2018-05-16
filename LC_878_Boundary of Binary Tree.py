'''

Given a binary tree, return the values of its boundary in anti-clockwise direction starting from root. Boundary includes left boundary, leaves, and right boundary in order without duplicate nodes.

Left boundary is defined as the path from root to the left-most node. Right boundary is defined as the path from root to the right-most node. If the root doesn't have left subtree or right subtree, then the root itself is left boundary or right boundary. Note this definition only applies to the input binary tree, and not applies to any subtrees.

The left-most node is defined as a leaf node you could reach when you always firstly travel to the left subtree if exists. If not, travel to the right subtree. Repeat until you reach a leaf node.

The right-most node is also defined by the same way with left and right exchanged.

Example
Given
  1
   \
    2
   / \
  3   4

return
[1, 3, 4, 2]

Explanation:
The root doesn't have left subtree, so the root itself is left boundary.
The leaves are node 3 and 4.
The right boundary are node 1,2,4. Note the anti-clockwise direction means you should output reversed right boundary.
So order them in anti-clockwise without duplicates and we have [1,3,4,2].
Given
         1
   /          \
  2            3
 / \          / 
4   5        6   
   / \      / \
  7   8    9  10  
       
return
[1,2,4,7,8,9,10,6,3]

Explanation:
The left boundary are node 1,2,4. (4 is the left-most node according to definition)
The leaves are node 4,7,8,9,10.
The right boundary are node 1,3,6,10. (10 is the right-most node).
So order them in anti-clockwise without duplicate nodes we have [1,2,4,7,8,9,10,6,3].

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
    @param root: a TreeNode
    @return: a list of integer
    """
    def boundaryOfBinaryTree(self, root):
        # write your code here
        #BFS
        if not root:
            return([])
        
        if not root.left:
            leftBound = [root]
        else:
            leftBound = []
            dummy = root
            while dummy:
                leftBound.append(dummy)
                if dummy.left:
                    dummy = dummy.left
                else:
                    dummy = dummy.right
        if not root.right:
            rightBound=[root]
        else:
            rightBound = []
            dummy = root
            while dummy:
                rightBound.append(dummy)
                if dummy.right:
                    dummy = dummy.right
                else:
                    dummy = dummy.left
              
        rightBound = rightBound[1:][::-1]
        
        leave =[] 
        
        stack = [root]
        while stack:
            node = stack.pop()
            
            if not node.left and not node.right:
                leave.append(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        out = [node.val for node in leftBound]
        leaveVal = [node.val for node in leave]
    
        if leftBound[-1] == leave[0]:
            out += leaveVal[1:]
        else:
            out+= leaveVal
        
        if rightBound and rightBound[0] == leave[-1]:
            rightBound = rightBound[1:]
       
        out += [node.val for node in rightBound]
    
        return(out)
        
        
