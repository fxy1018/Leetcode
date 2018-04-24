'''

There is a list of sorted integers from 1 to n. Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.

Repeat the previous step again, but this time from right to left, remove the right most number and every other number from the remaining numbers.

We keep repeating the steps again, alternating left to right and right to left, until a single number remains.

Find the last number that remains starting with a list of length n.

Example:

Input:
n = 9,
1 2 3 4 5 6 7 8 9
2 4 6 8
2 6
6

Output:
6

'''
class Solution:
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        sign = 1
        nums = [x for x in range(1, n+1)]
        while n > 1:
            if sign == 1:
                tmpNums= []
                for i in range(1, len(nums), sign*2):
                    tmpNums.append(nums[i])
                nums = tmpNums
                sign = -1
            else:
                tmpNums = []
                for i in range(len(nums)-2, -1, sign*2):
                    tmpNums.append(nums[i])
                nums = tmpNums[::-1]
                sign = 1
            n = n//2
        return(nums[0])
        
class Solution:
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return(1)
        
        return(2*(n//2 + 1-self.lastRemaining(n//2)))
