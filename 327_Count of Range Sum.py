'''

Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i ≤ j), inclusive.

Note:
A naive algorithm of O(n2) is trivial. You MUST do better than that.

Example:

Input: nums = [-2,5,-1], lower = -2, upper = 2,
Output: 3 
Explanation: The three ranges are : [0,0], [2,2], [0,2] and their respective sums are: -2, -1, 2.

'''
##I like this one!!!
## merge sort use case!!!
class Solution:
    """
    @param nums: a list of integers
    @param lower: a integer
    @param upper: a integer
    @return: return a integer
    """
    def countRangeSum(self, nums, lower, upper):
        # write your code here
        self.count = 0
        sumArray = []
        sumArray.append(0)
        for i in range(1, len(nums)+1):
            sumArray.append(sumArray[i-1] + nums[i-1])
        
        self.mergeSort(sumArray, lower, upper) 
        return(self.count)
        
    def mergeSort(self, sumArray, lower, upper):
        if len(sumArray) == 1:
            if sumArray[0]>=lower and sumArray[0] <= upper:
                print(sumArray[0])
                self.count += 1 
            return(sumArray)
        index = len(sumArray)//2
        left = self.mergeSort(sumArray[:index], lower, upper)
        right = self.mergeSort(sumArray[index:], lower, upper)
        
        self.countRange(left, right, lower, upper)
        return(self.merge(left, right))
    
    def merge(self, left, right):
        res = []
        while left and right:
            if left[0] < right[0]:
                res.append(left[0])
                left = left[1:]
            else:
                res.append(right[0])
                right =right[1:]
                
        if left:
            res = res + left
        if right:
            ret = res + right

        return(res)
            
    def countRange(self, left, right, lower, upper):
        lenL = len(left)
        lenR = len(right)
        
        start = 0
        end = 0
        for i in range(lenR):
            curr = right[i]
            while start < lenL and curr - upper >= left[start]:
                start += 1 
            while end < lenL and curr - lower > left[end]:
                end +=1
        self.count += (end-start)
    
    
    
