"""

Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

"""



'''
Created on Feb 16, 2017

@author: fanxueyi
'''
class Solution(object):
    def addBinary1(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        if not a or not b:
            return(b or a)
        
        return(bin(int(a,2)+int(b,2))[2:])
        
        
        
    def addBinary2(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a or not b:
            return(b or a)
        
        res, carry = "", 0
        i, j = len(a) - 1, len(b) - 1
        while i > -1 or j >-1 or carry :
            val = (i > -1 and a[i]=="1") + (j > -1 and b[j] == "1"):
            carry, mod = divmod(val+carry, 2)
            res = str(mod) + res
            i -= 1
            j -= 1
        return(res)
        
    