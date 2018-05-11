'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

'''

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        negative = False
        if x < 0:
            negative = True
            x *= -1
        
        while x > 0:
            mod = x%10
            res = 10*res + mod
            x = (x-mod)//10
            
        if res >2**31-1 or res < -2**31:
            return(0)
        
        if negative:
            return(res*-1)
        return(res)
            
