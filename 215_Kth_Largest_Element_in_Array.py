'''
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note: 
You may assume k is always valid, 1 <= k <=array's length.

'''


'''
Created on Jan 14, 2017

@author: fanxueyi
'''

"""
class Solution(object):
    def findKthLargest(self, nums, k):
        '''
        :type nums: List[int]
        :type k: int
        :rtype: int
        '''
        #method1
        #nums.sort()
        #return(nums[-k])
        
        #method2: partition, quick sort
        
        self.quickSort(nums, 0, len(nums)-1)
        return(nums[-k])
        
    def quickSort(self, nums,first, n):
        if first < n:
            #choose first element aspivot 
            pos = self.partition(nums,first,n)
            self.quickSort(nums, first, pos-1)
            self.quickSort(nums, pos+1,n)
        
        
    def partition(self,nums,start,end):
        p = nums[start]
        i = start+1
        for j in range(i,end+1):
            if nums[j] < p:
                nums[i],nums[j] = nums[j], nums[i]
                i += 1
        nums[start], nums[i-1] = nums[i-1], nums[start]
        print(nums)
        return(i-1)
  
"""

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #method1
        #nums.sort()
        #return(nums[-k])
        
        #method2: partition, quick sort
        
        return(self.findKthSmallest(nums, len(nums)-k))
        
        
    def findKthSmallest(self, nums, k):
        if nums:
            #choose first element aspivot 
            n = len(nums)-1
            pos = self.partition(nums,0,n)
            if k < pos:
                return(self.findKthSmallest(nums[:pos], k))
            elif k > pos:
                return(self.findKthSmallest(nums[pos+1:],k-pos-1))
            else:
                return(nums[pos])
        
        
    def partition(self,nums,start,end):
        p = nums[start]
        i = start+1
        for j in range(i,end+1):
            if nums[j] < p:
                nums[i],nums[j] = nums[j], nums[i]
                i += 1
        nums[start], nums[i-1] = nums[i-1], nums[start]
        print(nums)
        return(i-1)
            
 
            
solution = Solution()
print(solution.findKthLargest([-1,2,0,6,1,8,4],1))