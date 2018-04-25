'''

There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

'''

class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, nums1, nums2):
        # write your code here
        m = len(nums1)
        n = len(nums2)

        if (m+n)%2 == 0:
            count = (m+n)//2
            r1 = self.helpFun(nums1,nums2, count)
            r2 = self.helpFun(nums1, nums2, count+1)
            return(( r1+r2 )/2)
        else:
            count = (m+n)//2+1
            return(self.helpFun(nums1,nums2, count))

    def helpFun(self, nums1, nums2, count):

        m = len(nums1)
        n = len(nums2)

        if m > n: #always assume m is equal or smaller than n
            return(self.helpFun(nums2, nums1, count))
        if m == 0:
            return(nums2[count-1])
        if count == 1:
            return(min(nums1[0], nums2[0]))

        p1 = min(count//2, m)
        p2 = count-p1
        mid1 = p1 - 1
        mid2 = p2 - 1

        if nums1[mid1] < nums2[mid2]:
            return(self.helpFun(nums1[mid1+1:], nums2, count-p1))

        elif nums1[mid1] > nums2[mid2]:
            return(self.helpFun(nums1, nums2[mid2+1:], count-p2))

        else:
            return(nums1[mid1])
