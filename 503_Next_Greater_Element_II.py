'''

Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

'''

class Solution(object):
#burce-force O(n^2)
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
   
#use stack to store the index, O(n)
    def nextGreaterElements2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        out = [-1] * len(nums) 
        stack = []
        for i in range(2*len(nums)-1, -1, -1):
            while stack and nums[stack[-1]]<= nums[i%len(nums)]:
                stack.pop()
            
            if stack:
                out[i%len(nums)] = nums[stack[-1]]
            stack.append(i%len(nums))
        
        return(out)
