"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

[show hint]

Hint:
Could you do it in-place with O(1) extra space?
Related problem: Reverse Words in a String II


"""


'''
Created on Jan 13, 2017

@author: fanxueyi
'''


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #no in-place
        if nums:
            for i in range(k%len(nums)):
                print(i)
                tmp = nums[-1]
                nums.insert(0, tmp)
                nums.pop()
 class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        l = len(nums)
        if k%l == 0:
            return
        step = k%l
        part1 = nums[:l-k]
        part2 = nums[l-k:]
        nums[:k] = part2
        nums[k:] = part1
        return

solution = Solution()
print(solution.rotate([1,2],2))
