'''
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:
[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.

similar: LC200
'''

class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return(0)
        
        row = len(grid)
        col = len(grid[0])
        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    count = self.bfs(i, j, grid, row, col)
                    res = max(res, count)
        
        #reverse gird
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "#":
                    grid[i][j] = 1
                    
        return(res)
    
    def bfs(self, i, j, grid, row, col):
        queue = [(i,j)]
        count = 0
        while queue:
            i, j = queue[0]
            count = count + 1
            queue = queue[1:]
            
            grid[i][j] = "#"
            
            if i < row-1:
                if grid[i+1][j] == 1 and (i+1, j) not in queue:
                    queue.append((i+1,j))
            if i > 0:
                if grid[i-1][j] == 1 and (i-1, j) not in queue:
                    queue.append((i-1,j))
            if j < col-1:
                if grid[i][j+1] == 1 and (i, j+1) not in queue:
                    queue.append((i,j+1))       
            if j > 0:
                if grid[i][j-1] == 1 and (i, j-1) not in queue:
                    queue.append((i,j-1))
                    
          
        return(count)
            
            
            
            
            
            
            
            
            
