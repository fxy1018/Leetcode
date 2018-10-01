class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0]*(n+1) for _ in range(n+1)]
        for i in range(2, n+1):
            for j in range(1, n-i+2):
                res = float('Inf')
                for z in range(j, i+j-1):
                    tmp = z + max(dp[j][z-1], dp[z+1][i+j-1])
                    res = min(res, tmp)
                dp[j][i+j-1]=res
        return(dp[1][n])
        
