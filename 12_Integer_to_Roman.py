
"""
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.

"""
'''
Created on Jan 21, 2017

@author: fanxueyi
'''

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_dict = ["I", "IV", "V", "IX", "X","XL","L", "XC", "C", "CD", "D", "CM", "M"]
        val = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        res = ""
        for i in range(12,-1,-1):
            if num >= val[i]:
                count = num//val[i]
                num %=val[i]
                res += roman_dict[i]*count
        
        return(res)