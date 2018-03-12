'''

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".


'''

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        pHash = {}
        for c in p:
            pHash[c] = pHash.get(c,0) + 1
        window = {}
        res = []
        for i in range(len(s)):            
            window[s[i]] = window.get(s[i], 0) + 1
            if i == len(p)-1 and self.isSame(window, pHash):
                res.append(i-len(p)+1)
            elif i > len(p) -1 :
                window[s[i-len(p)]] = window.get(s[i-len(p)]) - 1
                if self.isSame(window, pHash):
                    res.append(i-len(p)+1)
        return(res)
                
    def isSame(self, window, pHash):
        for key in window:
            if key not in pHash:
                if window[key] > 0:
                    return(False)
            elif window[key] != pHash[key]:
                return(False)
        return(True)
            
