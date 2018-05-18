'''
Given an array nums of length n and an array req of length k , you need to fold the array as required, and output the result of the fold.
1.If req[i] = 0 means you should fold from left to right
for example:

1 2 3 4 5 6 7 8  ==>   4 3 2 1
                       5 6 7 8
2.If req[i] = 1 means you should fold from right to left
for example:

1 2 3 4 5 6 7 8  ==>   8 7 6 5
                       1 2 3 4
More example:

fold from left to right
4 3 2 1  ==>  6 5
5 6 7 8       3 4
              2 1
              7 8


fold from right to left
6 5  ==>   8
3 4        1
2 1        4
7 8        5
           6
           3
           2
           7 
 Notice
n is power of two.
k is index.(e.g. n = 2^3 = 8，k = 3)
Have you met this question in a real interview? 
Example
Given array nums = [1, 2, 3, 4, 5, 6, 7, 8] and array req = [0, 0, 1]
change array in place to be [8, 1, 4, 5, 6, 3, 2, 7]

'''
class Solution:
    """
    @param nums: the original array
    @param req: the direction each time
    @return: the final folded array 
    """
    def folding(self, nums, req):
        # write your code here
        for i in range(len(req)):
            nums = self.helpFun(nums, int(len(nums)/(2**(i+1))), req[i])
        return(nums)
    
    def helpFun(self, nums, step, direction):
        change = []
        unchange = []
        if direction == 0:
            for i in range(0, len(nums),2*step): 
                change = nums[i:i+step][::-1] + change
                unchange.extend(nums[i+step: i+2*step])
        else:
            for i in range(0, len(nums), 2*step):
                unchange.extend(nums[i:i+step])
                change = nums[i+step: i+2*step][::-1] + change
        return(change + unchange)
