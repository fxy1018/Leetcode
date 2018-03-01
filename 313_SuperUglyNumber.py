'''

Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k. For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.

Note:
(1) 1 is a super ugly number for any given primes.
(2) The given numbers in primes are in ascending order.
(3) 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
(4) The nth super ugly number is guaranteed to fit in a 32-bit signed integer.

very similar to 264_UglyNumberII

'''

class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        points = {}
        for prime in primes:
            points[prime] = 0
        
        out = [1] * n
        
        for i in range(1, n):
            out[i] = min([out[points[prime]]*prime for prime in points])
            for prime in points:
                if out[i]==out[points[prime]]*prime:
                    points[prime] = points[prime] + 1
        return(out[-1])
