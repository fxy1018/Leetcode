'''

Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Restrictions:
The string consists of lower English letters only.
Length of the given string and k will in the range [1, 10000]

'''

class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if len(s) < k:
            return(s[::-1])
        if len(s) < 2*k:
            rev = s[0:k]
            return(rev[::-1] + s[k:])
        rev = s[0:k]
        return(rev[::-1] + s[k:2*k] + self.reverseStr(s[2*k:],k))
 class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s= list(s)
        for i in range( 0,len(s), 2*k):
            s[i:i+k] = reversed(s[i:i+k])
        
        return(''.join(s)) 
   
