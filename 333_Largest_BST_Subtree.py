"""

Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where largest means subtree with largest number of nodes in it.

Note:
A subtree must include all of its descendants.
Here's an example:
    10
    / \
   5  15
  / \   \ 
 1   8   7
The Largest BST Subtree in this case is the highlighted one. 
The return value is the subtree's size, which is 3.
Hint:

You can recursively use algorithm similar to 98. Validate Binary Search Tree at each node of the tree, which will result in O(nlogn) time complexity.
Follow up:
Can you figure out ways to solve it with O(n) time complexity?


"""

'''
Created on Mar 12, 2017

@author: fanxueyi
'''



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #method1: O(nlogn)
        if not root:
            return 0
        
        record = self.isValidBST(root)
        if record[0]:
            return record[1]

        return(max(self.largestBSTSubtree(root.left), self.largestBSTSubtree(root.right)))

    
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool, int
        """
         
        #in-order traversal, but some code is unnecessary. 
        if not root:
            return(True)
        
        stack = []
        preval = -float("Inf")
        current = root
        done = False
        count = 0
        while not done:
            if current:
                stack.append(current)
                current = current.left
            else:
                if(len(stack) >0 ):
                    current = stack.pop()
                    count += 1
                    if current.val <= preval:
                        return(False, count)
                    preval = current.val
             
                    # We have visited the node and its left 
                    # subtree. Now, it's right subtree's turn
                    current = current.right 

                else:
                    done = True
        return (True,count)



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution2(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        node, record = (self.helpFun(root))
        return(record[0])
        
        
    def helpFun(self, root):
        #method2 O(N)
        minValue = float("Inf")
        maxValue = -float("Inf")
        record = [ 0, minValue, maxValue]
        if not root:
            return(root, record)
        if not root.left and not root.right:
            minValue = min(minValue, root.val)
            maxValue = max(maxValue, root.val)
            record = [1, minValue, maxValue]
            return(root, record)
            
        #left record:
        leftNode, leftRecord = self.helpFun(root.left) 
        rightNode, rightRecord = self.helpFun(root.right)
        
        if leftNode == root.left and rightNode == root.right:
            if leftRecord[2] < root.val and rightRecord[1] > root.val:
                record = [leftRecord[0]+rightRecord[0]+1, min(leftRecord[1],root.val), max(rightRecord[2], root.val)]
                return(root, record)
    
        return((leftNode, leftRecord) if leftRecord[0] > rightRecord[0] else (rightNode, rightRecord))
   
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
class Solution(object):
    def LongestBSTSubtree(self, root):
        if not root:
            return(0)
        record = [None, None, None]
        node, size = self.postOrder(root, record)
        return(size)
    
    def postOrder(self, node, record):
        if not node:
            record[0] = 0
            record[1] = float("Inf")
            record[2] = -float("Inf")
            return(None,0)
        
        value = node.val      
        leftNode, lsize = self.postOrder(node.left, record)
        lSize, lMin, lMax = record[0], record[1], record[2]
        
        rightNode, rsize = self.postOrder(node.right, record)
        rSize, rMin, rMax = record[0], record[1], record[2]
        
        record[1] = min(lMin, value)
        record[2] = max(rMax, value)
        
        if node.left == leftNode and node.right == rightNode and lMax < value and rMin > value:
            record[0] = lSize + rSize + 1
            return(node, record[0])
        
        elif lSize > rSize:
            return(leftNode, lSize)
        else:
            return(rightNode, rSize)
            
        
        
        
        
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(1)
root.left.right = TreeNode(8)
root.right.right = TreeNode(7)

s=Solution()
print(s.LongestBSTSubtree(root))

    
