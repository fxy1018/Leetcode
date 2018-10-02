class Solution:
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return(0)
        result = 0
        row = len(grid)
        col = len(grid[0])
        gridRow = 0
        gridCol = [0] * col 
        
        for i in range(row):
            for j in range(col):
                #calculate row enemy
                if j==0 or grid[i][j-1] == "W":
                    gridRow = 0
                    k = j
                    while k<col and grid[i][k] != "W":
                        if grid[i][k]=="E":
                            gridRow += 1
                        k += 1
                #calculate col enemy   
                if i == 0 or grid[i-1][j] == "W":
                    gridCol[j]=0
                    k = i
                    while k < row and grid[k][j] != "W":
                        if grid[k][j]=="E":
                            gridCol[j] +=1
                        k += 1
                        
                if grid[i][j] == "0": 
                    result = max(gridRow + gridCol[j], result)
        return(result)
                    
                    
                    
                    
