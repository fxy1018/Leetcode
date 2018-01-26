'''
Created on Jan 26, 2018

@author: XFan

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11

'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root, num):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        #preorder
        if not root:
            return(0)
        self.res = 0
        self.preOrder(root, 0,  {0:1}, num)
        return(self.res)
    #time: O(N), space need to modify, create two more hash
    def preOrder(self, root, pathSum, sumHash,  num):
        if not root:
            return
        value = root.val
        newPathSum = pathSum + value
        target = newPathSum - num
        
        self.res += sumHash.get(target, 0) 
        
        sumHash[newPathSum] = sumHash.get(newPathSum, 0)+1
        
        newSumHash = sumHash.copy()
        newSumHashRight = sumHash.copy()
       

        self.preOrder(root.left, newPathSum, newSumHash, num)
        self.preOrder(root.right, newPathSum, newSumHashRight, num)

    def preOrder2(self, root, pathSum, sumHash,  num):
        if not root:
            return
        value = root.val
        newPathSum = pathSum + value
        target = newPathSum - num
        
        self.res += sumHash.get(target, 0) 
        
        sumHash[newPathSum] = sumHash.get(newPathSum, 0)+1

        self.preOrder(root.left, newPathSum, sumHash, num)
        self.preOrder(root.right, newPathSum, sumHash, num)
        
        sumHash[newPathSum] -= 1

            
            
        
# head = root = TreeNode(5)
# root.left = TreeNode(4)
# root.right = TreeNode(8)
# left = head.left 
# right = head.right
# left.left = TreeNode(11)
# right.left = TreeNode(13)
# right.right = TreeNode(4)
# left.left.left = TreeNode(7)
# left.left.right = TreeNode(2)
# right.right.left = TreeNode(5)
# right.right.right = TreeNode(1)
root = TreeNode(1)


s = Solution()
s.pathSum(root, 22)
s.pathSum(root, 0)
