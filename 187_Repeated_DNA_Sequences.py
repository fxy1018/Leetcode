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
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        #method1: hash
         if len(s) < 10:
            return([])
        
        sHash = {s[0:10]: 1}
        p1 = 1
        for i in range(10, len(s)):
            seg = s[p1:i+1]
            sHash[seg] = sHash.get(seg, 0) +1
            p1 += 1
        out = []
        for key in sHash:
            if sHash[key]  > 1:
                out.append(key)
        return(out)
#method2: 实际上我们的哈希表可以不用存整个子串，因为我们知道子串只有10位，且每一位只可能有4种不同的字母，那我们可以用4^10个数字来表示每种不同的序列，因为4^10=2^20<2^32所以我们可以用一个Integer来表示。具体的编码方法是用每两位bit表示一个字符。



s= Solution()
print(s.findRepeatedDnaSequences("AAAAAAAAAAA"))
