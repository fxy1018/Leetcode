'''
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

Note: You may assume that n is not less than 2 and not larger than 58.

'''
class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <=2:
            return(1)
        dp = [-1 for _ in range(n+1)]
        dp[1] = 1
        dp[2] = 1
        for i in range(3, n+1):
            tmp = 0
            for j in range(1, i):
                tmp = max(tmp, j*dp[i-j], j*(i-j))
            dp[i] = tmp
        return(max(dp))


dp[i]表示整数i拆分可以得到的最大乘积，则dp[i]只与dp[i - 2], dp[i - 3]两个状态有关

得到状态转移方程：

dp[x] = max(3 * dp[x - 3], 2 * dp[x - 2])
当x <= 3时，需要对结果进行特判。

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 3: return n - 1
        dp = [0] * (n + 1)
        dp[2], dp[3] = 2, 3
        for x in range(4, n + 1):
            dp[x] = max(3 * dp[x - 3], 2 * dp[x - 2])
        return dp[n]
