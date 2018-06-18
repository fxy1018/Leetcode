'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.

'''

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        #method1: brute-force o(n*m)
        if not matrix:
            return(False)
        
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == target:
                    return(True)
        return(False)
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if not matrix:
            return(False)
        
        row = len(matrix)
        col = len(matrix[0])
        left = top = 0
        right = col-1
        bottom = row -1
        
        while left < right-1 and top < bottom-1:
            colMid = (left + right)//2
            rowMid = (top + bottom)//2
            if matrix[rowMid][colMid] == target:
                return(True)
            if matrix[rowMid][colMid] > target:
                if matrix[colMid][top] <= target:
                    right = colMid 
                else:
                    right = colMid-1
                if matrix[rowMid][left] <= target:
                    bottom = rowMid
                else:
                    bottom = rowMid-1
                    
            if matrix[rowMid][colMid] < target:
                if matrix[colMid][bottom] >= target:
                    left = colMid 
                else:
                    left = colMid+1
                if matrix[rowMid][right] >= target:
                    top = rowMid
                else:
                    top = rowMid+1
 
        return(False)

#time: O(m+n)
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        if not matrix or not matrix[0]:
            return(False)
        #start from the righttop corner
        row = len(matrix)
        col = len(matrix[0])
        top = 0
        right = col-1
        
        while top < row and right >= 0:
            if matrix[top][right] == target:
                return(True)
            elif matrix[top][right] > target:
                right -=1
            else:
                top += 1
 
        return(False)
