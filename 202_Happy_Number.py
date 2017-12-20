'''

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

'''


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
#         seen = set()
#         while n not in seen:
#             seen.add(n)
#             n = sum([int(x) **2 for x in str(n)])
#         return n == 1
    

        unhappy = set()
        while n not in unhappy:
            unhappy.add(n)
            n = self.sumSquare(n)
            if n == 1:
                return(True)
            
        return(False)
        
        
    def sumSquare(self, n):
        out = 0
        while n > 0:
            digit = n%10
            out += digit ** 2
            n = (n-digit) /10
        return(out)
            
        
