'''

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.
Example:
Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:
The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.

'''

#method1: array: update O(1), sum O(n), ETL
class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.nums[i] = val

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        res = 0
        for z in range(i, j+1):
            res += self.nums[z]
        return(res)
        
#method2:segment Tree: update, sum: O(logN)
#for a array length n, total nodes are 2n-1, hight of tree is (log2(N))
import math
class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if len(nums)==0:
            height = 0
        else:
            height = math.ceil(math.log2(len(nums)))
        self.nums = nums
        self.segmentTree = [0] * (2*int(math.pow(2,height))-1)
        self._buildTree( 0, len(nums), 0)
        
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        diff = val - self.nums[i] 
        self._updateTree(i, diff, 0, len(self.nums), 0)
        self.nums[i] = val
        
        
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        
        return(self._sumHelp(j, 0 , len(self.nums), 0) - self._sumHelp(i-1, 0, len(self.nums), 0))
        
    def _sumHelp(self, index, l, r, curr):
        if index == -1:
            return(0)
        if index == len(self.nums)-1:
            return(self.segmentTree[0])
        mid = math.ceil((l+r)/2.0)
        if index == mid-1:
            return(self.segmentTree[2*curr+1])
        elif index > mid-1:
            return(self.segmentTree[2*curr+1] + self._sumHelp(index, mid, r, 2*curr+2))
        else:
            return(self._sumHelp(index, l, mid, 2*curr+1))
             
        
        
    
    def _buildTree(self, l, r, index):
        if r == 0:
            return
        if l+1 == r:
            self.segmentTree[index] = self.nums[l]
            return(self.nums[l])
        
        left = self._buildTree( l, math.ceil((l+r)/2.0), 2*index+1)
        right = self._buildTree( math.ceil((l+r)/2.0), r, 2*index+2)
        self.segmentTree[index] = left+right
        return(left+right)
        
        
    def _updateTree(self, i, diff, l, r, curr):
        self.segmentTree[curr] += diff
        if l +1 ==r:
            return
        mid = math.ceil((l+r)/2.0)
        if i > mid-1:
            self._updateTree(i, diff, mid, r, 2*curr+2)
        else:
            self._updateTree(i, diff, l, mid, 2*curr+1)   


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
