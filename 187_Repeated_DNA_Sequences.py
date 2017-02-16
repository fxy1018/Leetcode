"""

All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].


"""


'''
Created on Feb 15, 2017

@author: fanxueyi
'''

#hash to record all 10 bits sequence.
#Time complexity: O(n)

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s or len(s) < 11:
            return([])
        str_hash = {}
        for i in range(len(s)-9):
            str_hash[s[i:i+10]] = str_hash.get(s[i:i+10], 0) + 1
        res = []  
        print(str_hash)
        for key in str_hash:
            print(key)
            if str_hash[key] > 1:
                res.append(key)
        
        return(res)

s= Solution()
print(s.findRepeatedDnaSequences("AAAAAAAAAAA"))