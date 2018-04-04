'''

Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:
Input: [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Example 2:
Input: [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]

'''

class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        
        if not nums:
            return(res)
        
        start = nums[0]
        end = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == end + 1:
                end = nums[i]
            else:
                if start == end:
                    res.append(str(end))
                else:
                    res.append(str(start) + "->" + str(end))
                    
                start = nums[i]
                end = nums[i]
        
        if start == end:
            res.append(str(end))
        else:
            res.append(str(start) + "->" + str(end))
                    
        return(res)
