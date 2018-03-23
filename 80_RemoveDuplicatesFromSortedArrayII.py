'''
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.



'''

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return(0)
        curr = 0
        count = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[curr+1] = nums[i]
                curr += 1
                count = 1
            else:
                count += 1
                if count <= 2:
                    nums[curr+1] = nums[i]
                    curr += 1
                
        return(curr+1)
