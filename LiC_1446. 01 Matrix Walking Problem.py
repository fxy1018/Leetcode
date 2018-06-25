'''
Given an 01 matrix gird of size n*m, 1 is a wall, 0 is a road, now you can turn a 1 in the grid into 0, Is there a way to go from the upper left corner to the lower right corner? If there is a way to go, how many steps to take at least?

Example
Given a = [[0,1,0,0,0],[0,0,0,1,0],[1,1,0,1,0],[1,1,1,1,0]]，return 7.

Explanation:
Change `1` at (0,1) to `0`, the shortest path is as follows:
(0,0)->(0,1)->(0,2)->(0,3)->(0,4)->(1,4)->(2,4)->(3,4) There are many other options of length `7`, not listed here.
Given a = [[0,1,1],[1,1,0],[1,1,0]], return -1.

Explanation:
Regardless of which `1` is changed to `0`, there is no viable path.

'''

class Solution:
    """
    @param grid: The gird
    @return: Return the steps you need at least
    """
    def getBestRoad(self, grid):
        # Write your code here
        #try every 1 to 0 and bfs find the shortest path
        
        path = float('Inf')
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if self.isContinue(grid, i, j):
                        grid[i][j] = 0
                        path = min(path, self.bfs(grid))
                        grid[i][j] = 1
        
        if path == float('Inf'):
            return(-1)
        return(path)
    
    def bfs(self, grid):
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return(float('Inf'))
        
        visit = set([])    
        queue = [(0, 0, 0)]
        
        while queue:
            x, y, path = queue.pop(0)
            if x == len(grid)-1 and y == len(grid[0])-1:
                return(path)
            
            if x > 0 and (x-1, y) not in visit and grid[x-1][y] == 0:
                queue.append((x-1,y, path+1))
                visit.add((x-1,y))
            if y > 0 and (x, y-1) not in visit and grid[x][y-1] == 0:
                queue.append((x, y-1, path+1))
                visit.add((x,y-1))
            if y < len(grid[0])-1 and (x, y+1) not in visit and grid[x][y+1] == 0:
                queue.append((x, y+1, path+1))
                visit.add((x,y+1))
            if x < len(grid)-1 and (x+1, y) not in visit and grid[x+1][y] == 0:
                queue.append((x+1, y, path+1)) 
                visit.add((x+1,y))
            
        return(float('Inf'))
    
    def isContinue(self, grid, x, y):
        count = 0
        if x > 0 and grid[x-1][y] == 1:
            count += 1
                
        if y > 0 and grid[x][y-1] == 1:
            count += 1
        if y < len(grid[0])-1 and grid[x][y+1] == 1:
            count += 1
        if x < len(grid)-1 and grid[x+1][y] == 1:
            count += 1
        
        return(count < 3)
        
        
                
