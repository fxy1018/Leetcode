'''

Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.

You may assume each number in the sequence is unique.

Follow up:
Could you do it using only constant space complexity?

'''
#memory limit exceeded
class Solution:
    """
    @param preorder: List[int]
    @return: return a boolean
    """
    def verifyPreorder(self, preorder):
        # write your code here
        if not preorder:
            return(True)
        root = preorder[0]
        i = 1
        while i<len(preorder) and preorder[i] < root:
            i+=1
        
        for j in preorder[i:]:
            if j < root:
                return(False)
        return(self.verifyPreorder(preorder[1:i]) and self.verifyPreorder(preorder[i:]))

#use stack to solve
