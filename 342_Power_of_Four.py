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
    
#method2: bit
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
            
        bn = bin(num)[2:]
        
        count = bn[1:].count("0")
        
        if bn[0] == "1" and count %2==0 and len(bn) == count + 1:
            return(True)
        return(False)
    
 #method3: math

class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return(num > 0 and (math.log10(num)/math.log10(4) %1==0))
    
#method4: bit manipulation: num & (num - 1)可以用来判断一个数是否为2的次方数, 4的次方数的最高位的1都是计数位,只需"与上 (&)" 一个数(0x55555555) <==> 1010101010101010101010101010101, 如果得到的数还是其本身，则可以肯定其为4的次方数
class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return(num>0 and not num&(num-1)  and (num & 0x55555555)==num)
    
#method5: 在确定其是2的次方数了之后，发现只要是4的次方数，减1之后可以被3整除

class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return(num>0 and not num&(num-1)  and (num-1)%3 ==0)
    

        
