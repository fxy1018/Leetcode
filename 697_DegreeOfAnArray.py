'''
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.

'''

class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numHash = {}
        for i in range(len(nums)):
            if nums[i] in numHash:
                numHash[nums[i]][0] =  numHash[nums[i]][0] + 1
                numHash[nums[i]][1][1] = i
            else:
                numHash[nums[i]] = [1, [i, i]]
        
        degree = 0
        elements = []
        
        for n in numHash:
            if numHash[n][0] > degree:
                elements = [n]
                degree = numHash[n][0]
            elif numHash[n][0] == degree:
                elements.append(n)
        
        res = len(nums)
        for n in elements:
            res = min(numHash[n][1][1] - numHash[n][1][0]+1, res)
        return(res)
    
    


class Solution(object):
    def findShortestSubArray(self, nums):
        left, right, count = {}, {}, {}
        for i, x in enumerate(nums):
            if x not in left: left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1

        ans = len(nums)
        degree = max(count.values())
        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)

        return ans
