"""
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

"""



'''
Created on Jan 14, 2017

@author: fanxueyi
'''


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic1 = {}
        dic2 = {}
        
        for i in nums1:
            if i in dic1:
                dic1[i] +=1
            else:
                dic1[i] = 1
        for j in nums2:
            if j in dic2:
                dic2[j] +=1
            else:
                dic2[j] = 1
                
        keys1 = dic1.keys()
        out = []
        for key in keys1:
            if key in dic2:
                out.extend([key]*min(dic1[key], dic2[key]))

        return(out)   
    
    def modifed(self,nums1,nums2):
            
        dic1 = {}
        out = []
        
        for i in nums1:
            if i in dic1:
                dic1[i] +=1
            else:
                dic1[i] = 1
        for j in nums2:
            if j in dic1 and dic1[j] > 0:
                out.append(j)
                dic1[j] -= 1
        return(out)  
            
              
            
#If only nums2 cannot fit in memory, put all elements of nums1 into a HashMap, read chunks of array that fit into the memory, and record the intersections.

#If both nums1 and nums2 are so huge that neither fit into the memory, sort them individually (external sort), then read 2 elements from each array at a time in memory, record intersections.