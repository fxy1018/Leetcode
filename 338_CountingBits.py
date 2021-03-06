'''
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2].

Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.

'''

class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        #brute-force:  O(n*sizeof(integer))
        res = []
        for n in range(num+1):
            res.append(bin(n)[2:].count("1"))
        return(res)
class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        #dp+bit manipulation
        
        res = [0] * (num+1)
        
        for i in range(1, num+1):
            res[i] = res[i&i-1] + 1
        return(res)
