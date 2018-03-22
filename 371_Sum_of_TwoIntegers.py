'''
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.

'''

class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        mask = 0xFFFFFFFF
        while b != 0 :
            tmp1 = (a^b) & mask
            tmp2 = ((a&b) <<1) &mask
            a = tmp1
            b = tmp2
        return(a if a <= 0x7FFFFFFF else ~(a^mask))
    
    

            
