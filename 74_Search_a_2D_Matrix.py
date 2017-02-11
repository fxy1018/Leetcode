"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.

"""

'''
Created on Feb 10, 2017

@author: fanxueyi
'''

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return(False)

        row = len(matrix)
        col = len(matrix[0])
        
        col_arr = zip(*matrix)[0]
        top= 0
        bottom = row-1
        left = 0
        right = col-1
        #binary search for first col
        while top <= bottom:
            mid = (top+bottom)/2
            if col_arr[mid] < target:
                top = mid +1
            elif col_arr[mid] > target:
                bottom = mid-1
            else: 
                return(True)
        #binary search for the row
        mid = (top+bottom)/2
        target_row = matrix[mid]
        while left<=right:
            mid = (left+right)/2
            if target_row[mid] < target:
                left = mid + 1
            elif target_row[mid] > target:
                right = mid -1
            else:
                return(True)
        return(False) 
    
s = Solution()
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 11))