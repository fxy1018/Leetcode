'''

Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.

'''
class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.res = 0
        curr = [["."] * n  for _ in range(n)]
        self._helpFun( n, 0, curr)
        return(self.res)
           
    def _helpFun(self, n, index, curr):
        if index == n:
            self.res+=1
            return
        for j in range(n):
            if self._isAttatched(index, j, curr, n):
                continue
            else:
                curr[index][j] = "Q"
                self._helpFun( n, index+1, curr)
                curr[index][j] = "."
        return

    def _isAttatched(self, rowIndex, colIndex, curr, n):
        #check column
        for i in range(rowIndex):
            if curr[i][colIndex] == "Q":
                return(True)
        
        #check diagnal
        for i in range(rowIndex):
            for j in range(n):
                if curr[i][j] == "Q" and abs(rowIndex-i) == abs(colIndex-j):
                    return(True)
        return(False)
