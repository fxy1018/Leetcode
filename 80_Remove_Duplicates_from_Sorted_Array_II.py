'''
Created on Feb 1, 2017

@author: fanxueyi
'''


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #method1 : two pointers
        point1 = 0
        point2 = 1
        while point2 < len(nums):
            if nums[point1] == nums[point2]:
                if point2-point1 == 1:
                    point2 += 1
                else:
                    nums.remove(nums[point1])
            else:
                point1 = point2 
                point2 += 1
    
        return(len(nums))
         
 
        
        
s=Solution()
print(s.removeDuplicates([1,2,2,2,2,3]))      
        
    