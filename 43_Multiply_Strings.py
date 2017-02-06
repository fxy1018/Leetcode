"""

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.

Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

"""
'''
Created on Feb 6, 2017

@author: fanxueyi
'''

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        """
        #method1:
        res = int(num1)*int(num2)
        return(str(res))
        """
        product = [0] * (len(num1)+len(num2))
        pos = len(product)-1
        
        for n1 in reversed(num1):
            tempPos = pos
            for n2 in reversed(num2):
                product[tempPos] += int(n1)* int(n2)
                product[tempPos-1] += product[tempPos]/10
                product[tempPos] %= 10
                tempPos -=1
            pos -= 1
        
        pt = 0
        while pt < len(product)-1 and product[pt] == 0:
            pt +=1

        return("".join(map(str, product[pt:])))
        
        
