'''
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

'''

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        tHash = {}
        for c in t:
            tHash[c] = tHash.get(c, 0) + 1
            if c not in s or tHash[c] > s.count(c):
                return("")
	    
        for i in range(len(s)):
            if s[i] in tHash:
                left = i
                break
        right = left 
        loc = {}
        res = s
        count = len(t)
        while right < len(s):
            c = s[right]
            if c in tHash:
                if tHash[c] > 0: 
                    count -=1
                    tHash[c] -= 1
                    loc[c] = loc.get(c, []) + [right]
                else:
                    loc[c] = loc[c] + [right]
                    loc[c] = loc[c][1:]
                    if s[left] == c:
                        left = min([loc[key][0] for key in loc])
                        
                if count == 0:
                    if len(res) > len(s[left:right+1]):
                        res = s[left:right+1]

            right += 1
        return(res)
                        
                
