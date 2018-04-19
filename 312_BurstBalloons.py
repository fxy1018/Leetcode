'''

Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note: 
(1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
(2) 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

Example:

Given [3, 1, 5, 8]

Return 167

    nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
   coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
'''


class Solution:
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        l = len(nums)
        memo = [[-1]* l for _ in range(l)]
        return(self.getMemo(memo,nums, 1, l-2))
        
    
    def getMemo(self, memo, nums, start, end):
        if start == end:
            memo[start][end] = nums[start] 
            return(nums[start])
        if start > end:
            return(0)
        
        if memo[start][end] != -1:
            return(memo[start][end])
        
        tmp = 0
        for k in range(start, end+1):
            tmp = max(tmp, nums[k]* nums[start-1] * nums[end+1] + self.getMemo(memo, nums, start, k-1)+ self.getMemo(memo, nums, k+1, end))
        memo[start][end] = tmp
        return(memo[start][end])
        
   
   

