'''
Created on Feb 1, 2017

@author: fanxueyi
'''



class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0]*n for i in range(n)]
        left, right, top, bottom = 0, n-1, 0, n-1
        nums = [i for i in range(1,n**2+1)]
        nums.reverse()
        while(len(nums)>0):
            for col in range(left, right+1):
                num = nums.pop()
                matrix[top][col] = num
            top += 1
            
            for row in range(top, bottom+1):
                num = nums.pop()
                matrix[row][right] = num
            right -= 1
            
            for col in range(right, left-1, -1):
                num=nums.pop()
                matrix[bottom][col] = num
            bottom -=1
            
            for row in range(bottom, top-1, -1):
                num = nums.pop()
                matrix[row][left] = num
            left += 1
            
        return(matrix)
        
        
        