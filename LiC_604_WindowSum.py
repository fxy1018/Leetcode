'''
Given an array of n integer, and a moving window(size k), move the window at each iteration from the start of the array, find the sum of the element inside the window at each moving.

Have you met this question in a real interview? 
Example
For array [1,2,7,8,5], moving window size k = 3. 
1 + 2 + 7 = 10
2 + 7 + 8 = 17
7 + 8 + 5 = 20
return [10,17,20]

'''
class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):
        # write your code here
        if not nums:
            return([])
            
        l = len(nums)
        if k >=l:
            return([sum(nums)])
            
        res = [sum(nums[:k])]
        for i in range(k, l):
            t = res[-1] + nums[i] - nums[i-k]
            res.append(t)
        return(res)
