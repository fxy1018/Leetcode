"""

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum >= s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

click to show more practice.

More practice:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).

"""

'''
Created on Mar 3, 2017

@author: fanxueyi
'''

#method1: use two pointers: time: O(n)
#定义两个指针left和right，分别记录子数组的左右的边界位置，然后我们让right向右移，直到子数组和大于等于给定值或者right达到数组末尾，此时我们更新最短距离，并且将left像右移一位，然后再sum中减去移去的值，然后重复上面的步骤，直到right到达末尾，且left到达临界位置，即要么到达边界，要么再往右移动，和就会小于给定值。
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        if n == 0:
            return 0 
            
        left = 0
        right = 0
        
        res = n + 1
        temp_sum = 0
        while right < n:
            while temp_sum < s and right < n:
                temp_sum += nums[right]
                right += 1

            while temp_sum >=s:
                res = min(res, right-left)
                temp_sum -= nums[left]
                left += 1
                
        if res == n + 1 :
            return(0)
        else:
            return(res)



#method2: binary search:  time o(nlogn)
#我们建立一个比原数组长一位的sums数组，其中sums[i]表示nums数组中[0, i - 1]的和，然后我们对于sums中每一个值sums[i]，用二分查找法找到子数组的右边界位置，使该子数组之和大于sums[i] + s，然后我们更新最短长度的距离即可。
class Solution2(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        if n == 0:
            return 0 
        
        res = n + 1
        sum_pos =[0]
        
        for i in range(1, n + 1):
            sum_pos.append(sum_pos[i-1] + nums[i-1])
            
        for i in range(n + 1):
            key_sum = sum_pos[i] + s
            pos = self.binarySearch(i+1, n+1 , sum_pos, key_sum)
            if pos:
                res = min(res, pos-i)
                
        if res != n + 1:
            return(res)
        
        else:
            return(0)
        
    def binarySearch(self, left, right, sum_pos, n):
        if sum_pos[-1] < n:
            return(None)
        
        while left <= right:
            mid = (left+right)//2 
            if sum_pos[mid] >= n:
                right = mid - 1
        
            else:
                left = mid + 1
                
        return(left)
        
        
s = Solution2()
print(s.minSubArrayLen(7, [2,3,1,2,4,3]))