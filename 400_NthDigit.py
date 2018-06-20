'''
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:

Input:
3

Output:
3
Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.

'''

class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 10:
            return(n)
        digit = 1
        while n - 9*digit*10**(digit-1)  >  0:
            n -= 9*digit*10**(digit-1)
            digit+=1
        div,mod = divmod(n, digit)
        div = 10**(digit-1) + div-1
        if mod == 0:
            return(int(str(div)[-1]))
        else:
            return(int(str(div+1)[mod-1]))
