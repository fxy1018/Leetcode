"""

given a stack, return reversed stack (in-place)

"""

'''
Created on Mar 4, 2017

@author: fanxueyi
'''

class Solution(object):
    def popFistElementOfStack(self, stack):
        num = stack.pop()
        if not stack:
            return(num)
        return(self.popFistElementOfStack(stack))
    
    def reverseStack(self, stack):
        num = stack.pop()
        if not stack:
            return([num])
        return([num] + self.reverseStack(stack))
         
 
s = Solution()
print(s.popFistElementOfStack([7,3,2,1,5,6])) 
print(s.reverseStack([3,2,1,0]))      