"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?


"""



'''
Created on Mar 25, 2017

@author: fanxueyi
'''


class Solution(object):
    #O(N^2) DP 解法
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return(0)
            
        dp = [1] * len(nums)
        
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        
        return(max(dp))
    
    
    #O(nlogN) 解法， binary serach
    #我们先建立一个数组ends，把首元素放进去，然后比较之后的元素，如果遍历到的新元素比ends数组中的首元素小的话，替换首元素为此新元素，如果遍历到的新元素比ends数组中的末尾元素还大的话，将此新元素添加到ends数组末尾(注意不覆盖原末尾元素)。如果遍历到的新元素比ends数组首元素大，比尾元素小时，此时用二分查找法找到第一个不小于此新元素的位置，覆盖掉位置的原来的数字，以此类推直至遍历完整个nums数组，此时ends数组的长度就是我们要求的LIS的长度，特别注意的是ends数组的值可能不是一个真实的LIS，比如若输入数组nums为{4, 2， 4， 5， 3， 7}，那么算完后的ends数组为{2， 3， 5， 7}，可以发现它不是一个原数组的LIS，只是长度相等而已，千万要注意这点。
    def lengthOfLIS2(self,nums):
    
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return(0)
            
        ends = [nums[0]]
        r = 0
        for i in range(1,len(nums)):
            left = 0
            right = len(ends)-1
            while (left <= right):
                mid = (left+right)//2
                if ends[mid] < nums[i]:
                    left = mid + 1
                else:
                    right = mid - 1
           
            if left >= len(ends):
                ends.append(nums[i])
            else:
                ends[left] = nums[i]
        
        return(len(ends))

s=Solution()
print(s.lengthOfLIS2([10, 9, 2, 5, 3, 7, 101, 18]))
