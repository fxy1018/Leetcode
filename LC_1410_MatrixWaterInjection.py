'''
Given a two-dimensional matrix, the value of each grid represents the height of the terrain. The flow of water will only flow up, down, right and left, and it must flow from the high ground to the low ground. As the matrix is surrounded by water, it is now filled with water from (R,C) and asked if water can flow out of the matrix.

Example
Given

mat =
[
    [10,18,13],
    [9,8,7],
    [1,2,3]
]
R = 1, C = 1, return "YES"。

Explanation:
(1,1) →(1,2)→Outflow.
Given

mat = 
[
    [10,18,13],
    [9,7,8],
    [1,11,3]
]
R = 1, C = 1, return "NO"。

Explanation:
Since (1,1) cannot flow to any other grid, it cannot flow out.

'''

class Solution:
    """
    @param matrix: the height matrix
    @param R: the row of (R,C)
    @param C: the columns of (R,C)
    @return: Whether the water can flow outside
    """
    def waterInjection(self, matrix, R, C):
        # Write your code here
        if not matrix:
             return("NO")
        row = len(matrix)
        col = len(matrix[0])
        if R >= row or C >=col:
            return("NO")
        visit = set([])  
        return(self.helpFun(matrix, R, C, row, col, visit))
    
    def helpFun(self, matrix, R, C, row, col, visit):
        if R == row-1 or C == col-1:
            return("YES")
        
        curr = matrix[R][C]
        if (R-1, C) not in visit and matrix[R-1][C] < curr and self.helpFun(matrix, R-1, C, row, col, visit) == "YES":
            visit.add((R-1,C))
            return("YES")
        if (R, C-1) not in visit and matrix[R][C-1] < curr and self.helpFun(matrix, R, C-1, row, col, visit) == "YES":
            visit.add((R,C-1))
            return("YES")
        if (R+1, C) not in visit and matrix[R+1][C] < curr and self.helpFun(matrix, R+1, C, row, col, visit) == "YES":
            visit.add((R+1,C))
            return("YES")
        if (R, C+1) not in visit and matrix[R][C+1] < curr and self.helpFun(matrix, R, C+1, row, col, visit) == "YES":
            visit.add((R,C+1))
            return("YES")
            
        return("NO")
        
