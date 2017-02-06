"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

Note:
You can assume that you can always reach the last index.

"""


'''
Created on Feb 6, 2017

@author: fanxueyi
'''

#http://www.cnblogs.com/lichen782/p/leetcode_Jump_Game_II.html
#扫描数组以确定当前最远能覆盖的节点，放入curr。然后继续扫描，直到当前的路程超过了上一次算出的覆盖范围
#那么更新覆盖范围，同时更新跳数，因为我们是经过了多一跳才能继续前进的。

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        currMax = 0
        njump = 0
        last = 0
        for i in range(n):
            if (i>last):
                last  = currMax
                njump += 1
            
            currMax = max(currMax, i+nums[i])
        
        return(njump)
        
