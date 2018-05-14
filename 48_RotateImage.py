'''
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]


'''
class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        row = len(matrix)
        for i in range(row):
            for j in range(i, row-i-1):
                pos1 = [i,j]
                pos2 = [j, row-i-1]
                pos3 = [row-i-1, row-j-1]
                pos4 = [row-j-1, i]
                num1 = matrix[pos1[0]][pos1[1]]
                num2 = matrix[pos2[0]][pos2[1]]
                num3 = matrix[pos3[0]][pos3[1]]
                num4 = matrix[pos4[0]][pos4[1]]
                matrix[pos1[0]][pos1[1]] = num4
                matrix[pos2[0]][pos2[1]] = num1
                matrix[pos3[0]][pos3[1]] = num2
                matrix[pos4[0]][pos4[1]] = num3
        return
                  
  
  
  
