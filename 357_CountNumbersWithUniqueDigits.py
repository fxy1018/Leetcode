'''
Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:
Given n = 2, return 91. (The answer should be the total numbers in the range of 0 ≤ x < 100, excluding [11,22,33,44,55,66,77,88,99])

'''

class Solution:
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        #math
        if n >10:
            n = 10
        if n == 0:
            return(1)
        if n == 1:
            return(10)
        res = 10
        pre = 9
        for i in range(2, n+1):
            pre = pre*(10-i+1)
            res += pre
        
        return(res)
