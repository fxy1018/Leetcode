"""
no extra space, swap two value

"""

'''
Created on Mar 18, 2017

@author: fanxueyi
'''


#bit manipularion

class Solution(object):
    '''
    input: int, int
    rType: int, inte
    '''
    
    def swap(self,a,b):
        a = a^b
        b = a^b
        a = a^b
        
        return(a,b)

s = Solution()
print(s.swap(3,4))
print(s.swap(0,-2))