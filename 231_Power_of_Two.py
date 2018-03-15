'''

Given an integer, write a function to determine if it is a power of two.

'''

#method1: recursion
class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return(False)
        
        if n == 1:
            return(True)
    
        div, mod = divmod(n, 2)
        
        if mod == 1:
            return(False)
        return(self.isPowerOfTwo(div))
        
#method2: bit count
class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <=0:
            return(False)
        return(bin(n)[2:].count("1") == 1)
        
#method2: bit shift
class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
    
        if n <=0:
            return(False)
        
        count = 0
        for i in range(32):
            if count > 1:
                return(False)
            if n & 1 == 1:
                count += 1
            n >>= 1
        return(count == 1)
        
 #method3: bit manipulation,  bin of power of two is 1 following all 0 and bin of power of two -1 is 0 following all of 1, n&n-1 == 0
class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return( n> 0 and not(n&n-1))
        
