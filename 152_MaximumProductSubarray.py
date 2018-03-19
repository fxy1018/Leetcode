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

#dp: consider neg * neg = pos, pon*neg = new; use two arrays to record max and min number if must be end at index i 
class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return(0)
        
        l = len(nums)
        dpMin = [0] * l
        dpMax = [0] * l
        
        dpMax[0] = dpMin[0] = res = nums[0]
        
        for i in range(1, l):
            preMin = dpMin[i-1]
            preMax = dpMax[i-1]
            if nums[i] < 0:
                dpMax[i] = max(preMin*nums[i], nums[i])
                dpMin[i] = min(preMax*nums[i], nums[i])  
            else:
                dpMax[i] = max(preMax*nums[i], nums[i])
                dpMin[i] = min(preMin*nums[i], nums[i])  
            res = max(dpMax[i], res)
        return(res)
    
    
#method3: compress space
#dp: consider neg * neg = pos, pon*neg = new; use two arrays to record max and min number if must be end at index i 
class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return(0)

        preMin = preMax = res = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] < 0:
                tmpMax = max(preMin*nums[i], nums[i])
                tmpMin = min(preMax*nums[i], nums[i])  
            else:
                tmpMax = max(preMax*nums[i], nums[i])
                tmpMin = min(preMin*nums[i], nums[i])
                
            preMin = tmpMin
            preMax = tmpMax
            res = max(preMax, res)
        return(res)
 
#dp: consider neg * neg = pos, pon*neg = new; use two arrays to record max and min number if must be end at index i 
class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return(0)

        preMin = preMax = res = nums[0]
        
        for n in nums[1:]:
            if n < 0:
                tmpMax = max(preMin*n, n)
                tmpMin = min(preMax*n, n)  
            else:
                tmpMax = max(preMax*n, n)
                tmpMin = min(preMin*n, n)
                
            preMin = tmpMin
            preMax = tmpMax
            res = max(preMax, res)
        return(res)
