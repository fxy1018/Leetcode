'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

'''

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        s_t_dict = {}
        n = len(s)
        for i in range(n):
            if s[i] not in s_t_dict:
                if t[i] in s_t_dict.values():
                    return(False)
                else:
                    s_t_dict[s[i]] = t[i]
            else:
                if s_t_dict[s[i]]!= t[i]:
                    return(False)
        return(True)
