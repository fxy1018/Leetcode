'''

Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?

'''

class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #for loop
        
        while n >= 3:
            n, mod = divmod(n, 3)
            if mod != 0:
                return(False)
        if n == 1:
            return(True)
        else:
            return(False)
import math
class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #math
        if n <=0:
            return(False)
        return(math.log10(n) / math.log10(3) %1 == 0)
