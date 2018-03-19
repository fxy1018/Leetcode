'''

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.


当我们判断以某个点为正方形右下角时最大的正方形时，那它的上方，左方和左上方三个点也一定是某个正方形的右下角，否则该点为右下角的正方形最大就是它自己了。
这是定性的判断，那具体的最大正方形边长呢？我们知道，该点为右下角的正方形的最大边长，最多比它的上方，左方和左上方为右下角的正方形的边长多1，
最好的情况是是它的上方，左方和左上方为右下角的正方形的大小都一样的，这样加上该点就可以构成一个更大的正方形。       
但如果它的上方，左方和左上方为右下角的正方形的大小不一样，合起来就会缺了某个角落，这时候只能取那三个正方形中最小的正方形的边长加1了。

'''
class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        #for dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1, 
        if not matrix:
            return(0)
        
        row = len(matrix)
        col = len(matrix[0])
        
        dp = [ [0] * col for _ in range(row)]
        
        res = 0
           
        for i in range(row):
            if matrix[i][0] == "1":
                dp[i][0] = 1 
                res = 1
    
        for j in range(1, col):
            if matrix[0][j] == "1":
                dp[0][j] = 1 
                res = 1
        
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                res = max(res, dp[i][j])
        
       
        return(res*res)
        
        
