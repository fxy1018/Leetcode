'''
You are given a 0-indexed m x n binary matrix grid.

A 0-indexed m x n difference matrix diff is created with the following procedure:

Let the number of ones in the ith row be onesRowi.
Let the number of ones in the jth column be onesColj.
Let the number of zeros in the ith row be zerosRowi.
Let the number of zeros in the jth column be zerosColj.
diff[i][j] = onesRowi + onesColj - zerosRowi - zerosColj
Return the difference matrix diff.
'''
class Solution(object):
    def onesMinusZeros(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """

        rowNum = len(grid)
        columnNum = len(grid[0])

        rowStat = [[0, 0] for i in range(rowNum)]
        columnStat = [[0, 0] for i in range(columnNum)]

        # Start traverse the grid to get stat number
        for i in range(rowNum):
            rowStat[i] = [columnNum-sum(grid[i]), sum(grid[i])]
        for j in range(columnNum):
            columnSum = self.getColumnSum(grid, j, rowNum)
            columnStat[j] = [rowNum-columnSum, columnSum]

        output = [[0 for j in range(columnNum)] for i in range(rowNum)]
        
        for i in range(rowNum):
            for j in range(columnNum):
                output[i][j] = rowStat[i][1] + columnStat[j][1] - rowStat[i][0] - columnStat[j][0]
        return output

    def getColumnSum(self, grid, j, rowNum):
        total = 0
        for i in range(rowNum):
            total += grid[i][j]
        return total
        
