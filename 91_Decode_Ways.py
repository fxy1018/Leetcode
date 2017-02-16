"""


A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.

"""


'''
Created on Feb 16, 2017

@author: fanxueyi
'''

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        #处理边界， 当string为空，或者是“0” 的时候
        if len(s) == 0 or s[0] < "1" :
            return(0)
            
        dp = [0 for i in range(len(s)+1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(1,len(s)):
            val = int(s[i-1])*10 + int(s[i])
            if val > 9 and val <=26:
                dp[i+1] = dp[i-1]
            if s[i] != "0":
                dp[i+1] += dp[i]
        
        return(dp[-1])
        
        


        
        