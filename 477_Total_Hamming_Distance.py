#The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

#Now your job is to find the total Hamming distance between all pairs of the given numbers.

#Note:
#Elements of the given array are in the range of 0 to 10^9
#Length of the array will not exceed 10^4.
#Hide Company Tags

'''
Created on Jan 5, 2017

@author: fanxueyi
'''

class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # use zip and map and string format to finish
        out = sum(i.count("0") * i.count("1") for i in zip(*map('{:032b}'.format, nums)))
        
        return(out)
        
        
        # bit
        
        bits = [[0,0] for i in xrange(32)]
        for x in nums:
            for i in xrange(32):
                bits[i][x%2] += 1
                x /= 2
        return(sum(x*y for x,y in bits))
            