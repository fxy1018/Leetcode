'''

Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

'''

class Solution(object):
#burce-force
    def nextGreaterElements1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        out = [-1] * len(nums)
        for i in range(len(nums)):
            newNums = nums[i:] + nums[0:i]
            for n in range(1,len(newNums)):
                if newNums[n] > nums[i]:
                    out[i] = newNums[n]
                    break
        return(out)
   
