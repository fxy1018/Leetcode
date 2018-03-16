'''
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
'''

class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # brute-force: O(n**3)
        if not nums:
            return(0)
        
        l = len(nums)
        res = nums[0]
        for i in range(l):
            for j in range (i, l):
                if i == j:
                    res = max(res, nums[i])
                else:
                    product = 1
                    for z in range(i, j+1):
                        product *= nums[z]
                    res = max(res, product)
        return(res)
                    
