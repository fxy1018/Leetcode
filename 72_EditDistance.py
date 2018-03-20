'''
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character

#Classic DP: 构建n*m矩阵，位置[i,j]标示串T1[0,i]和T2[0,j]的编辑距离。

显而易见的是，对于矩阵中的i,j位置，他可以有如下三种方式变换： 
1、从i-1,j 为T1增加一个字符，获得i，j，这样编辑距离本身就需要+1 
2、同理，从i，j-1过来，编辑距离必须+1。 
3、从i-1，j-1位置变换过来，那么这个时后，如果T1在i的取值和T2在j的取值一样，那么这个变换，编辑距离不变，如果不一样，那么就需要做替换操作，那么必须+1.
'''

class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(word1) + 1
        m = len(word2) + 1
        
        dp = [[0] * n  for _ in range(m)]
        
        for i in range(n):
            dp[0][i] = i
        
        for j in range(m):
            dp[j][0] = j
        
        for i in range(1,m):
            for j in range(1, n):
                if word1[j-1] == word2[i-1]:
                    tmp= dp[i-1][j-1]
                else:
                    tmp = dp[i-1][j-1] + 1
                dp[i][j] = min(dp[i][j-1] + 1, dp[i-1][j]+ 1, tmp)       
        return(dp[m-1][n-1])


import unittest
class TestSolution(unittest.TestCase):
    def test_longword(self):
        s = Solution()
        word1 = "pneumonoultramicroscopicsilicovolcanoconiosis"
        word2 = "ultramicroscopically"
        self.assertEqual(s.minDistance(word1, word2), 27) 
    def test_shortword(self):
        s = Solution()
        word3 = "sea"
        word4 = "eat"
        self.assertEqual(s.minDistance(word3, word4), 2)
    def test_NA(self):
        s=Solution()
        word1 =""
        word2=""
        self.assertEqual(s.minDistance(word1, word2), 0)
