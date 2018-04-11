'''
Given a matrix of size n x m, the elements in the matrix are 0、1、2. 0 for the sea, 1 for the island, and 2 for the city on the island(You can assume that 2 is built on 1, ie 2 also represents the island).
If two 1 are adjacent, then these two 1 belong to the same island. Find the number of islands with at least one city.

 Notice
We only consider up, down, left and right as adjacent.
n <= 100，m <= 100.
You can assume that the four sides of the matrix are surrounded by the sea.

Example
Given mat =
[
     [1,1,0,0,0],
     [0,1,0,0,1],
     [0,0,0,1,1],
     [0,0,0,0,0],
     [0,0,0,0,1]
]
, return 0.

Explanation:
There are 3 islands, but none of them contain cities.
Given mat =
[
     [1,1,0,0,0],
     [0,1,0,0,1],
     [0,0,2,1,2],
     [0,0,0,0,0],
     [0,0,0,0,2]
]
, return 2.

Explanation:
There are 3 islands, and two of them have cities.
'''

class Solution:
    """
    @param grid: an integer matrix
    @return: an integer 
    """
    def numIslandCities(self, grid):
        # Write your code here
        if not grid:
            return(0)
            
        row = len(grid)
        col = len(grid[0])
        
        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    res += 1
                    self._bfs(i, j, grid, row, col)
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 3:
                    grid[i][j] == 1
                if grid[i][j] == 4:
                    grid[i][j] == 2
        
        return(res)
    
    def _bfs(self, rowI, colI, grid, row, col):
        queue = [(rowI, colI)]
        while queue:
            i, j = queue[0]
            queue = queue[1:]
            if grid[i][j] == 1:
                grid[i][j] = 3
            if grid[i][j] == 2:
                grid[i][j] = 4
                
            if i > 0:
                if grid[i-1][j] == 1 or grid[i-1][j] == 2:
                    queue.append((i-1, j))
            if i < row-1:
                if grid[i+1][j] == 1 or grid[i+1][j] == 2:
                    queue.append((i+1, j))
            if j > 0:
                if grid[i][j-1] == 1 or grid[i][j-1] == 2:
                    queue.append((i, j-1))
            if j < col-1:
                if grid[i][j+1] == 1 or grid[i][j+1] == 2:
                    queue.append((i, j+1))
