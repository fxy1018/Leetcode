"""

Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

"""
'''
Created on Feb 6, 2017

@author: fanxueyi
'''

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        #add digit of num1, and num2 one by one. 
        
        if len(num1) < len(num2):
            num1,num2 = num2,num1
        num1 = num1[::-1]
        num2 = num2[::-1]
        num2 += "0"*(len(num1)-len(num2))
        
        sum_two = [0]
        Pos = len(sum_two)-1
        
        for i in range(len(num2)):
            digit_sum = int(num1[i])+int(num2[i])+sum_two[-1]
            div, mod = divmod(digit_sum,10)
            sum_two[-1] = mod
            sum_two.append(div)
        if sum_two[-1] == 0:
            sum_two.pop()
            
        out = ''.join(map(str, sum_two[::-1]))
        return(out)
    
        
        
        
s= Solution()
print(s.addStrings("9", "99"))