"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

[
  ["aa","b"],
  ["a","a","b"]
]

"""

'''
Created on Mar 16, 2017

@author: fanxueyi
'''
class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return([])
        res = []
        curr = []
        palHash= set([]) 
        self._helpFun(s, res,curr,palHash)
        print(palHash)
        return(res)
    
    def _helpFun(self, s, res, curr, palHash):
        if not s:
            res.append(curr)
            return
        
        l = len(s)
        for i in range(l):
            part1 = s[0:i+1]
            part2 = s[i+1:]
            if part1 in palHash or part1 == part1[::-1]:
                palHash.add(part1)
                newCurr= curr + [part1]
                self._helpFun(part2, res, newCurr, palHash) 
            else:
                continue

