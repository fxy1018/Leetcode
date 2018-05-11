"""
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note: All inputs will be in lower-case.

"""
'''
Created on Feb 6, 2017

@author: fanxueyi
'''

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        #method1: use hash to store sorted str, and key is sorted str, value is actual str
        """
        方法一:设置一个HashMap,key为同组字符串按照字典序重新重新排列之后的字符串,比如:”ate”, “eat”,”tea”,对于该组的字符串,如果对字符串里面的字符按照字典顺序重新排列之后,那么都将为”aet”,这样的话,我们把”aet”作为key,value为原始字符串如果重新排列之后为该key的所有字符串,显然,这些字符串组成了一个字符串列表。
        
        """
        
        strs_hash = {}
        for s in strs:
            s_sort = "".join(sorted(s))
            if s_sort not in strs_hash:
                strs_hash[s_sort] = [s]
            else:
                strs_hash[s_sort].append(s)
        
        out = []
        for s in strs_hash:
            out.append(strs_hash[s])
        
        return(out)
    
        #method2:
        """
        方法二:这个方法很巧妙的一点是利用了素数的性质,素数数组的意思代表26个字母,我们想想,如果把字符串每个位置上面的字母转化成相应的素数,并累成起来,那么相同组的字符串肯定结果相同,不同组的字符串肯定结果不同
        """
        
         
  class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        #method1:
        
        strHash = {}
        for s in strs:
            sortedS = sorted(list(s))
            sortedS = "".join(sortedS)
            
            strHash[sortedS] = strHash.get(sortedS, []) + [s]
        
        res = []
        for key in strHash:
            res.append(strHash[key])
        return(res)          
        
