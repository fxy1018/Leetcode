class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        left = 0
        right = len(nums)-1
        return(self.help(nums, left, right) >=0)
    
    def help(self, nums, left, right):
        if left == right:
            return(nums[left])
        
        return(max(nums[left]-self.help(nums, left+1, right), nums[right]-self.help(nums, left, right-1)))
        
        
class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return(False)
    
        left = 0
        right = len(nums)
        dp =  [[0] * right for _ in range(right)]
        for i in range(right):
            dp[i][i] = nums[i]
        
        
        for i in range(right-2, -1, -1):
            for j in range(i+1, right):
                dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])
        
        return(dp[0][-1] >=0)
