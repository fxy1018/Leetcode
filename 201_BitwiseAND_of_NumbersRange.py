'''
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4.

'''
class Solution:
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        #brute-force (TLE)
        numArray = range(m, n+ 1)
        res = numArray[0]
        for i in range(1,len(numArray)):
            res = res & numArray[i]
        return(res)
        
        
            
 class Solution:
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        #bit
        i = 0
        while m != n:
            m >>=1
            n >>=1
            i += 1
        return n << i
            
