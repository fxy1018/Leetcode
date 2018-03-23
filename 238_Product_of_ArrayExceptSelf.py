'''

Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)


'''


#pre-modify the array
class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        leftProduct = [1] * len(nums) 
        rightProduct = [1] * len(nums) 
        
        for j in range(len(nums)-2, -1, -1):
            rightProduct[j] = rightProduct[j+1] * nums[j+1]
        res = [rightProduct[0]] * len(nums)
        
        for i in range(1, len(nums)):
            leftProduct[i] = leftProduct[i-1] * nums[i-1]
            res[i] = leftProduct[i] * rightProduct[i]
       
        return(res)

#pre-modify the array, compress space
class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        leftProduct = 1
        rightProduct = [1] * len(nums) 
        
        for j in range(len(nums)-2, -1, -1):
            rightProduct[j] = rightProduct[j+1] * nums[j+1]
        
        for i in range(1, len(nums)):
            leftProduct *= nums[i-1]
            rightProduct[i] = leftProduct * rightProduct[i]
       
        return(rightProduct)
