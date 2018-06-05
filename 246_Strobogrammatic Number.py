'''

A mirror number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is mirror. The number is represented as a string.

Have you met this question in a real interview?  
Example
For example, the numbers "69", "88", and "818" are all mirror numbers.
Given num = "69" return true
Given num = "68" return false

'''

class Solution:
    """
    @param num: a string
    @return: true if a number is strobogrammatic or false
    """
    def isStrobogrammatic(self, num):
        # write your code here
        numHash= {'6':'9', '9':'6', '8':'8', '1':'1', '0':'0'}
        rotateNum = ""
        for n in num:
            if n not in numHash:
                return(False)
            rotateNum = numHash[n] + rotateNum
        
        return(rotateNum == num)
