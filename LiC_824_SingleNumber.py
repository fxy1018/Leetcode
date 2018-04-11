'''
Give an array, all the numbers appear twice except one number which appears once and all the numbers which appear twice are next to each other. Find the number which appears once.

 Notice
1 <= nums.length < 10^4
In order to limit the time complexity of the program, your program will run 10^5 times.

Example
Given nums = [3,3,2,2,4,5,5], return 4.

Explanation:
4 appears only once.
Given nums = [2,1,1,3,3], return 2.

Explanation:
2 appears only once.

'''
class Solution:
    """
    @param nums: The number array
    @return: Return the single number
    """
    # O(n)
    def getSingleNumber(self, nums):
        # Write your code here
        n = nums[0]
        for i in range(1, len(nums)):
            n = n^nums[i]
        return(n)
        
    #O(logN)
 class Solution:
    """
    @param nums: The number array
    @return: Return the single number
    """
    def getSingleNumber(self, nums):
        # Write your code here
        l = 0
        r = len(nums)-1
        
        while l < r:
            mid = (l+r)//2
            if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                return(nums[mid])
            
            elif nums[mid] == nums[mid-1]:
                left = mid-l + 1
                if left%2 ==0:
                    l = mid + 1
                else:
                    r = mid -2
            elif nums[mid] == nums[mid+1]:
                right = r - mid + 1

                if right%2==0:
                    r = mid-1
                else:
                    l = mid + 2
                   
        return(nums[l])
                   
