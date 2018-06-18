'''
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
Example 1: 
Input:

0 0 0
0 1 0
0 0 0
Output:
0 0 0
0 1 0
0 0 0
Example 2: 
Input:

0 0 0
0 1 0
1 1 1
Output:
0 0 0
0 1 0
1 2 1
Note:
The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.

'''
class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        
        #bfs, check four direction
        
        if not matrix or not matrix[0]:
            return(matrix)
        
        row = len(matrix)
        col = len(matrix[0])
        
        res = [[False]* col for _ in range(row)]
        
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    res[i][j] = 0
                else:
                    res[i][j] = self.bfs(matrix, i , j)
        return(res)
    
    def bfs(self, matrix, i, j):
        queue = [(i,j, 0)]
        visit = set([])
        while queue:
            currI, currJ, level = queue.pop(0)
            if matrix[currI][currJ] == 0:
                return(level)
            #left
            if currJ > 0 and (currI, currJ-1) not in visit:
                visit.add((currI, currJ-1))
                queue.append((currI, currJ-1, level +1))
            
            #right
            if currJ < len(matrix[0])-1 and (currI, currJ+1) not in visit:
                visit.add((currI, currJ+1))
                queue.append((currI, currJ+1, level +1))
            
            #up
            if currI > 0 and (currI-1, currJ) not in visit:
                visit.add((currI-1, currJ))
                queue.append((currI-1, currJ, level +1))
            
            #down
            if currI < len(matrix)-1 and (currI+1, currJ) not in visit:
                visit.add((currI+1, currJ))
                queue.append((currI+1, currJ, level +1))
        
