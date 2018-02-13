'''
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 6.

'''

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        res = 0
        if not matrix:
            return(res)
        row = len(matrix)
        col = len(matrix[0])
        newMatrix = [matrix[0]]
        lastRow = [0] * col
        for i in range(row):
            newRow = []
            for j in range(col):
                if matrix[i][j] == "0":
                    newRow.append(0)
                else:
                    newRow.append(lastRow[j]+1)
            res = max(res, self.getMax(newRow))
            lastRow = newRow
        
        return(res)
            
    def getMax(self, heights):
        res = 0
        stack = [-1]
        heights.append(0)
        n = len(heights)
        for i in range(n):
            curr = heights[i]
            while stack[-1]!=-1 and heights[stack[-1]]>= curr:
                index = stack.pop()
                res = max(res, heights[index]*(i-stack[-1]-1))
            stack.append(i)
        return(res)
