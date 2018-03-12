'''
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.

'''

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)
        set2 = set(nums2)
        res = []
        for n in set1:
            if n in set2:
                res.append(n)
        return(res)
        
    def intersection(self,nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1&set2)
        
