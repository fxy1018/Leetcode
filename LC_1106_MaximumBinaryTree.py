'''
Description
Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

The size of the given array will be in the range [1,1000].

Have you met this question in a real interview?  
Example
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1

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
    @param nums: an array
    @return: the maximum tree
    """
    def constructMaximumBinaryTree(self, nums):
        # Write your code here
        if not nums:
            return(None)
        if len(nums) == 1:
            return(TreeNode(nums[0]))
        
        maxNum = max(nums)
        for i in range(len(nums)):
            if nums[i] == maxNum:
                if i == 0:
                    left = None
                else:
                    left = nums[:i]
                if i == len(nums)-1:
                    right = None
                else:
                    right = nums[i+1:]
                break
            
        root = TreeNode(maxNum)
        root.left = self.constructMaximumBinaryTree(left)
        root.right= self.constructMaximumBinaryTree(right)
        
        return(root)
