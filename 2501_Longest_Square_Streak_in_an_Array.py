'''
You are given an integer array nums. A subsequence of nums is called a square streak if:

The length of the subsequence is at least 2, and
after sorting the subsequence, each element (except the first element) is the square of the previous number.
Return the length of the longest square streak in nums, or return -1 if there is no square streak.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

'''


class Solution(object):
    def longestSquareStreak(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        used = set()
        output = 1

        for num in sorted(nums):
            if num in used:
                continue
            count = 1
            used.add(num)
            while (num**2 in nums):
                used.add(num**2)
                num *= num
                count += 1
            output = max(count, output)
        return output if output>1 else -1
            
