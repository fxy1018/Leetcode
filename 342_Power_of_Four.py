'''

Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?

'''
#method1: recursion
class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 4:
            if num == 1:
                return(True)
            else:
                return(False)
            
        div, mod = divmod(num, 4)
        if mod != 0:
            return(False)
        return(self.isPowerOfFour(div))
        
