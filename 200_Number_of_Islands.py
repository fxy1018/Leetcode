"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

"""

'''
Created on Jan 15, 2017

@author: fanxueyi
'''
# graph connection problem use DFS OR BFS can finish it. 

class Solution(object):
    def __init__(self):
        self.nrow = 0
        self.ncol = 0
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0])==0:
            return(0)
            
        self.nrow =  len(grid)
        self.ncol =  len(grid[0])
        
        out = 0
        queue = []
        
        for i in range(self.nrow):
            for j in range(self.ncol):
                if grid[i][j] == "1":
                    out += 1
                    #bsf traversal the land and set visited land as 0
                    queue.append((i,j))
                    self.bsf(grid, queue)
                    
        return(out)
                
                
                
    def bsf(self, grid, queue):
        while queue:
            i,j = queue.pop(0)
            grid[i][j] = "0"
            # top, left, bottom, right, check whether it is 1
            if i > 0:
                if grid[i-1][j] == "1" and ((i-1,j) not in queue):
                    queue.append((i-1,j))
            if j > 0:
                if grid[i][j-1] == "1"and ((i,j-1) not in queue):
                    queue.append((i,j-1))
            if i < self.nrow-1 and ((i+1,j) not in queue):
                if grid[i+1][j] == "1":
                    queue.append((i+1,j))
            if j < self.ncol-1 and ((i,j+1) not in queue):
                if grid[i][j+1] == "1":
                    queue.append((i,j+1))

        
         
    #consice code:
    
    def numIslands2(self, grid):
        def sink(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
                grid[i][j] = '0'
                map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1))
                return 1
            return 0
        return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))
                    
                
    
