class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #dp
        row = len(s)
        col = len(t)
        dp = [[False] * (col+1) for _ in range(row+1)]
        for j in range(col+1):
            dp[0][j] = True
        for i in range(1, row+1):
            for j in range(1, col+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-1]  
        return(dp[-1][-1])
        
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #我们可以用两个指针分别指向字符串s和t，然后如果字符相等，则i和j自增1，反之只有j自增1，最后看i是否等于s的长度，等于说明s已经遍历完了，而且字符都有在t中出现过
        if not s:
            return(True)
        if not t:
            return(False)
        
        p1 = p2 = 0
        while p2 < len(t):
            if t[p2] != s[p1]:
                p2 += 1
            else:
                p1 += 1 
                p2 += 1
                if p1 == len(s):
                    return(True)
        return(False)
