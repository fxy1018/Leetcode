'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

'''

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return(0)
        add = 0
        for i in range(len(digits)-1, -1 , -1):
            if i == len(digits)-1:
                curr = digits[i] + 1 + add
            else:
                curr = digits[i] + add
                
            if curr > 9 :
                add, mod = divmod(curr, 10)
                digits[i] = mod
            else:
                digits[i] = curr
                add = 0
                
        if add == 1:
            return([1]+digits)
        
        return(digits)
        
                
        
