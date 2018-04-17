'''


Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.

'''
#dp, dp[i][j] = (dp[i-1][j] == True and s2[i-1] == s3[i+j-1]) or (dp[i][j-1] == True and s1[j-1] == s3[i+j-1])
class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)
        
        if l3 != l1 + l2:
            return(False)
        
        dp = [[False]*(l1+1) for _ in range(l2+1)]
        dp[0][0] = True
        for j in range(1, l1+1):
            dp[0][j] = dp[0][j-1] and s1[j-1]==s3[j-1]
        
        for i in range(1, l2+1):
            dp[i][0] = dp[i-1][0] and s2[i-1]==s3[i-1]
        
        for i in range(1, l2+1):
            for j in range(1, l1+1):
                dp[i][j] = (dp[i-1][j] == True and s2[i-1] == s3[i+j-1]) or (dp[i][j-1] == True and s1[j-1] == s3[i+j-1])
        return(dp[-1][-1])
