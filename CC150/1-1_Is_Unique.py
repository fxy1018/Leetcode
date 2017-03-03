'''
Created on Mar 2, 2017

@author: fanxueyi
'''
from symbol import xor_expr


class Solution(object):
    #assume acsII string
    #hash map 
    def isUnique(self, string):
        if len(string) > 128:
            return(False)
        string_hash = {}
        for s in string:
            if s in string_hash:
                return(False)
            else:
                string_hash[s] = 1
        return(True)
    
    #no additional data structure:
    #sort the file and compare 
    def isUnique2(self, string):
        sorted_str = sorted(string)
        for i in range(len(sorted_str)-1):
            if sorted_str[i] == sorted_str[i+1]:
                return(False)
        return(True)
    
    
string = "akdlfewjlra"
s = Solution()
print(s.isUnique(string))
print(s.isUnique2(string))
