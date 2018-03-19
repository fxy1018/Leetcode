'''
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.

'''
#method1: DP: dp[i] = Math.max(dp[j] + dp[i-j], dp[i], ETL
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return(1)
    
        dp = [float("Inf")] * (n+1)
        for i in range(1, n+1):
            if i*i <= n:
                dp[i*i] = 1
            if dp[i] == 1:
                continue
            for j in range(1, (i//2)+1):
                dp[i] = min(dp[j] + dp[i-j], dp[i])
        return(dp[-1])

#method1: DP: dp[i + j * j] = Math.min(dp[i] + 1, dp[i + j * j]), ETL
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [float("Inf")] * (n+1)
        
        for i in range(int(math.sqrt(n))+1):
            dp[i*i] = 1
        
        for i in range(1, n+1):
            j = 1
            while i+j*j <=n:
                dp[i+j*j] = min(dp[i]+1, dp[i+j*j])
                j+=1

        return(dp[n])
#method3: 这道题是考察四平方和定理
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        while n%4 == 0:
            n /= 4
        if n%8 == 7:
            return(4)
        
        if math.sqrt(n) % 1== 0.0:
            return(1)
        for a in range(int(math.sqrt(n)) + 1):
            b = math.sqrt(n- a*a)
            if b % 1 == 0.0:
                return(2)
        return(3)
