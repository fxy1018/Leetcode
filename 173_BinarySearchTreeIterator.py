'''
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.

'''

# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#in-order iteration
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return(len(self.stack) > 0)
        
    def next(self):
        """
        :rtype: int
        """
        if self.hasNext:
            node = self.stack.pop()
            tmp = node.right
            while tmp:
                self.stack.append(tmp)
                tmp = tmp.left
            return(node.val)
        else:
            return(None)
    
# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node 
"""

#space: O(n)
class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    def __init__(self, root):
        # do intialization if necessary
        self.tree = []
        self.stack = []
        while root or self.stack:
            if root:
                self.stack.append(root)
                root = root.left
            else:
                root = self.stack.pop()
                self.tree.append(root)
                root = root.right
            
        self.tree = self.tree[::-1]
    """
    @return: True if there has next node, or false
    """
    def hasNext(self, ):
        # write your code here
        if self.tree:
            return(True)
        else:
            return(False)
    """
    @return: return next node
    """
    def next(self, ):
        # write your code here
        if self.tree:
            return(self.tree.pop())
        else:
            return()
