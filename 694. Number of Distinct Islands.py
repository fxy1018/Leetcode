class Solution:
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        #record relative position
        isLandHash = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    tmp = self.bfs(i, j, grid)
                    isLandHash.add(tmp)
        return(len(isLandHash))
    
    def bfs(self, x, y, grid):
        queue = [(x,y,0,0)]
        visited = set((x,y))
        res = []
        while queue:
            currX, currY, relX, relY = queue.pop(0)
            res.append((relX, relY))
            grid[currX][currY] = 2
            if currX > 0 and (currX-1,currY) not in visited and grid[currX-1][currY]== 1:
                queue.append((currX-1, currY, relX-1, relY))
                visited.add((currX-1,currY))
            if currY > 0 and (currX,currY-1) not in visited and grid[currX][currY-1]== 1:
                queue.append((currX, currY-1, relX, relY-1))
                visited.add((currX,currY-1))
            if currX < len(grid)-1 and (currX+1,currY) not in visited and grid[currX+1][currY]== 1:
                queue.append((currX+1, currY, relX+1, relY))
                visited.add((currX+1,currY))
            if currY <len(grid[0])-1 and (currX,currY+1) not in visited and grid[currX][currY+1]== 1:
                queue.append((currX, currY+1, relX, relY+1))
                visited.add((currX,currY+1))
        return(tuple(res))
                
                
                
                
                
                
                
