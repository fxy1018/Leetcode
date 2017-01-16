"""

Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button  to reset your code definition.

spoilers alert... click to show requirements for atoi.

Requirements for atoi:
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.


"""


'''
Created on Jan 16, 2017

@author: fanxueyi
'''

import re

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        
    
        #ord("0") - ord("9") : 48-57
        str = str.strip()
        regOut = re.search(r'^([\+\-0]*\d+)\D*', str)
        if regOut:
            str = regOut.group(1)
        else:
            return(0)
        numList = []
        out = 0
        sign = 1
        sign_num = 0
        for i in str:
            if i == "-":
                sign = -1
                sign_num += 1
            elif i =="+":
                sign_num += 1
            else:
                numList.append(ord(i))
        if sign_num >= 2:
            return(0)
        print(sign_num, sign)   
        print(numList)
        #numList = [i for i in numList if i>=48 and i <=57]
        
        for i in range(len(numList), 0, -1):
            
            out += (numList[len(numList)-i]-48)*10**(i-1)
            
        out = sign * out
        
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        if out >= INT_MAX  or out <= INT_MIN:
            return(INT_MAX or INT_MIN)
        else:    
            return(out)


s = Solution()
print(s.myAtoi("+1"))




