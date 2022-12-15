'''
You are given an m x n matrix grid consisting of positive integers.

Perform the following operation until grid becomes empty:

Delete the element with the greatest value from each row. If multiple such elements exist, delete any of them.
Add the maximum of deleted elements to the answer.
Note that the number of columns decreases by one after each operation.

Return the answer after performing the operations described above.
'''

class Solution(object):
    def deleteGreatestValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        column = len(grid[0])

        sortedGrid = [sorted(arr) for arr in grid]
        output = 0
        for j in range(column):
            arrTemp = []
            for i in range(row):
                arrTemp.append(sortedGrid[i][j])
            output += max(arrTemp)
        return output
        
