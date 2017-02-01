"""

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].


"""


'''
Created on Jan 30, 2017

@author: fanxueyi
'''

"""
转圈打印矩阵，需要设置left, right, top和bot四个变量来控制， 注意每次增加行/列前要判断list所含元素是否小于矩阵的总元素数目。需要再想办法简化一下。
Time Complexity - O(mn)， Space Complexity - O(1)
"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return(matrix)
            
        rowM = len(matrix)
        colM = len(matrix[0])
        total = rowM * colM
        left, right, top, bottom = 0, colM-1, 0, rowM-1
        res = []
        while len(res)< total:
            for col in range(left, right+1):
                res.append(matrix[top][col])
            top+=1
            
            if(len(res)<total):
                for row in range(top,bottom+1):
                    res.append(matrix[row][right])
                right -=1
            
            if(len(res)<total):
                for col in range(right,left-1,-1):
                    res.append(matrix[bottom][col])
                bottom -=1
            if(len(res)<total):
                for row in range(bottom, top-1, -1):
                    res.append(matrix[row][left])
                left +=1
        return(res)
            
        


