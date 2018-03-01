'''

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number, and n does not exceed 1690.

思路：

我们来看看，要如何求第n个ugly number.

第一个ugly number 是1 我们讨论n大于1的情况

因为它只能被2，3，5整除，所以我们从1开始扩展，每次要么乘2，要么乘3，要么乘5.

对于1来说，我们分别乘以2，3，5得到[2,3,5]，显然2是最小的。

于是第2个ugly number是2。

接着第3个呢？显然是 3 . 从 1 * 3 得到

第4个就不一样了，它是从2*2得到。

这有什么规律呢？规律就是，每个因子分别乘以当前得到的ugly number（初始为1），当某因子x算出来的不大于其他两个因子，说明新的ugly number是当前因子算出来的，下一轮，该因子应该乘以之前ugly number的下一个。

换句话说，每个因子分别乘以对应的ugly number[i]后，如果得到了新的ugly number 就说明下一次应该乘以下一个（ugly number[i+1]）。这样能保证乘出来的小而且不会漏掉。
'''


class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        a = b= c=0
        ugly = [1] * n
        for i in range(1, n):
            ugly[i] = min(ugly[a]*2,ugly[b]*3,ugly[c]*5)
            if ugly[a]*2 == ugly[i]:
                a += 1
            if ugly[b]*3 == ugly[i]:
                b += 1
            if ugly[c]*5 == ugly[i]:
                c += 1
        return(ugly[-1])
