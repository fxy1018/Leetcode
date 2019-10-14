class Solution(object):
    def __init__(self):
        self.res = 0
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        depth = len(nums)
        currSum = 0
        currDepth = 0
        
        self.dfs(nums, S, currSum, currDepth, depth)
        return(self.res)
    
    
    def dfs(self, nums, S, currSum, currDepth, depth):
        if currDepth == depth:
            if currSum == S: 
                self.res += 1
            return
        #left node +1
        self.dfs(nums, S, currSum+nums[currDepth], currDepth+1, depth)
        self.dfs(nums, S, currSum-nums[currDepth], currDepth+1, depth)
        
        
class Solution(object):
    def __init__(self):
        self.res = 0
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        depth = len(nums)
        currSum = 0
        currDepth = 0
        memo = [[-float("Inf")]*2001 for i in range(len(nums))]
        return(self.dfs(nums, S, currSum, currDepth, memo))
    
    def dfs(self, nums, S, currSum, currDepth, memo):
        if currDepth == len(nums):
            if currSum == S: 
                return(1)
            return(0)
        
        if memo[currDepth][currSum+1000] != -float("Inf"):
            return(memo[currDepth][currSum+1000])
        
        add = self.dfs(nums, S, currSum+nums[currDepth], currDepth+1, memo)
        substract = self.dfs(nums, S, currSum-nums[currDepth], currDepth+1, memo)
        
        memo[currDepth][currSum+1000] = add+substract
        return(memo[currDepth][currSum+1000])
