"""

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

"""

'''
Created on Feb 27, 2017

@author: fanxueyi
'''


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        #method: use matrix to record DP result
        row = len(triangle)
        col = len(triangle[-1])
        
        dp = [[float("Inf")]*col for i in range(row)]
        
        #initialize the dp
        dp[0][0] = triangle[0][0]

        for j in range(1,row):
            dp[j][0] = dp[j-1][0] + triangle[j][0]
        
        for i in range(1,row):
            for j in range(1, len(triangle[i])):
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
        
        return(min(dp[-1]))
    
    def minimumTotal2(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        #method:  O(n) extra space
        row = len(triangle)

        dp = [[float("Inf")]*len(triangle[i]) for i in range(row)]
        
        #initialize the dp
        dp[0][0] = triangle[0][0]

        for j in range(1,row):
            dp[j][0] = dp[j-1][0] + triangle[j][0]
        
        for i in range(1,row):
            for j in range(1, len(triangle[i])):
                if j != len(triangle[i]) -1 :
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
                else:
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
        
        return(min(dp[-1]))
    
    

s = Solution()
print(s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))