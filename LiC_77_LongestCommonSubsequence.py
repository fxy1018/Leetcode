'''
Given two strings, find the longest common subsequence (LCS).

Your code should return the length of LCS.

Clarification
What's the definition of Longest Common Subsequence?

https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
http://baike.baidu.com/view/2020307.htm
Example
For "ABCD" and "EDCA", the LCS is "A" (or "D", "C"), return 1.

For "ABCD" and "EACB", the LCS is "AC", return 2.

# dp[i][j] means the longest common subsequence of A[0:i], B[0:j]
dp[i][j] = max(dp[i-1][j-1]+1?A[i]==B[j]:0, dp[i-1][j], dp[i][j-1])
'''

class Solution:
    """
    @param A: A string
    @param B: A string
    @return: The length of longest common subsequence of A and B
    """
    def longestCommonSubsequence(self, A, B):
        # write your code here
        if not A or not B:
            return(0)
        
        l1 = len(A)
        l2 = len(B)
        
        dp = [[0]*l1 for _ in range(l2)]
        
        count = 0
        for j in range(l1):
            if A[j] == B[0]:
                dp[0][j] = 1
                count = 1
            else:
                dp[0][j] = count
            
        count = 0 
        for i in range(l2):
            if A[0] == B[i]:
                dp[i][0] = 1
                count = 1
            else:
                dp[i][0] = count
            
        for i in range(1, l2):
            for j in range(1, l1):
                if A[j] == B[i]:
                    tmp1 = dp[i-1][j-1] + 1
                else:
                    tmp1 = dp[i-1][j-1]
                dp[i][j] = max(tmp1, dp[i-1][j], dp[i][j-1])
                
        return(dp[-1][-1])
