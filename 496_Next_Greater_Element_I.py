'''
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

'''

class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        
        out = []
        
        for num in findNums:
            i = 0
            while nums[i] != num:
                i += 1
            j = i + 1
            while j < len(nums):
                if nums[j] > num:
                    out.append(nums[j])
                    break
                j += 1
            if j == len(nums):
                out.append(-1)
        return(out)
        
     def nextGreaterElement2(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        #use stack to keep a decreasing sub-sequence
        out = []
        num_map = {}
        stack = []
        for num in nums:
            while stack and stack[-1] < num:
                curr = stack.pop()
                num_map[curr] = num
            stack.append(num)
        
        for num in findNums:
            if num not in num_map:
                out.append(-1)
            else:
                out.append(num_map[num])
        return(out)
