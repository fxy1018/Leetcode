"""
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.

"""

'''
Created on Jan 13, 2017

@author: fanxueyi
'''

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        out = 0
        i = 1
        while n//(5**i) >= 1:
            out += n//(5**i)
            i += 1
        return(out)