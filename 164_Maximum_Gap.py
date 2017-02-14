"""

Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.

"""

'''
Created on Feb 14, 2017

@author: fanxueyi
'''

class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #use bucket sort method
        if len(nums) <2:
            return(0)
        n = len(nums)
        bucket = [[] for i in range(n+1)]
        num_min = min(nums)
        num_max = max(nums)
        if num_min == num_max:
            return(0)
        
        for i in range(n):
            if nums[i] == num_max:
                bucket[-1].append(num_max)
            elif nums[i] == num_min:
                bucket[0].append(num_min)
            else:
                bucket_index = (nums[i]-num_min)*n/(num_max-num_min)
                bucket[bucket_index].append(nums[i])
        res = 0
        left = max(bucket[0])
        empty = 0
        for i in range(1,n+1):
            if bucket[i] == []:
                if empty == 0:
                    left = max(bucket[i-1])
                    empty += 1
                else:
                    empty +=1
            elif empty > 0 :
                res = max(res, (min(bucket[i])-left))
                left = max(bucket[i])
                empty = 0
        
        return(res)
    

#same strategy, diff write method, use three arrays to record all bucket information
class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #use bucket sort method
        if len(nums) <2:
            return(0)
        n = len(nums)
        num_min = min(nums)
        num_max = max(nums)
        if num_min == num_max:
            return(0)
            
        #modified
        hasNum = [False for i in range(n+1)]
        maxs = [0 for i in range(n+1)]
        mins = [0 for i in range(n+1)]
        bucket_index = 0
        for i in range(n):
            bucket_index = self.bucket(nums[i], n, num_min, num_max)
            mins[bucket_index] = min(mins[bucket_index], nums[i]) if hasNum[bucket_index] else nums[i]
            maxs[bucket_index] = max(maxs[bucket_index], nums[i]) if hasNum[bucket_index] else nums[i]
            hasNum[bucket_index] = True
        res = 0
        lastMax = maxs[0]
        for i in range(1,n+1):
            if hasNum[i]:
                res = max(res, mins[i]-lastMax)
                lastMax = maxs[i]
        return(res)
        
    def bucket(self,num, len, min, max):
        return((num-min)*len/(max-min)) 
        #for python 2, will return int automatically
                
            
            
            
            
                
            
                
                
                
            
            
            
            