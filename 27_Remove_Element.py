'''
Created on Jan 13, 2017

@author: fanxueyi
'''


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        
        p1 = 0
        p2 = len(nums)-1
        
        while p1 <= p2:
            if nums[p1] == val:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                nums.pop()
                p2 -= 1
            else: 
                p1 += 1

        
                
        return(nums)
            
        
solution = Solution()
print(solution.removeElement([2,2,2], 0))
