"""
Write a function to find the longest common prefix string amongst an array of strings.

"""
'''
Created on Jan 13, 2017

@author: fanxueyi
'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return("")
        
        zipped = zip(*strs)
        out = ""
        for i, group in enumerate(zipped):
            if len(set(group)) > 1 :
                return(strs[0][:i])
            
        return(min(strs))
            