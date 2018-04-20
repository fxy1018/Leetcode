'''
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
Note:
The input string length won't exceed 1000.


'''


class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        #dp[i][j] means whether s[i:j] is palindrom, dp[i][j] = s[i] == s[j] and dp[i+1][j-1] ==True
        if not s:
            return(0)
        
        l = len(s)
        dp = [[0] * l for _ in range(l)]
        count = 0
        for i in range(l-1, -1, -1):
            for j in range(l-1, i-1, -1):
                if i==j or s[i] == s[j] and (i+1 == j or dp[i+1][j-1] ==1):
                    dp[i][j] = 1
                    count += 1
        return(count)
                         

