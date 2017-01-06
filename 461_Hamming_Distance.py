#The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

#Given two integers x and y, calculate the Hamming distance.

#Note:
#0 ≤ x, y < 231.

'''
Created on Jan 5, 2017

@author: fanxueyi
'''

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        #bin_x = bin(x)[2:]
        #bin_y = bin(y)[2:]
        
        #if len(bin_x) <= len(bin_y):
        #    bin_x = "0" * (len(bin_y) - len(bin_x)) + bin_x
        #else:
        #    bin_y = "0" * (len(bin_x) - len(bin_y)) + bin_y
            
        #count = 0
        #for i in range(len(bin_x)):
        #    if bin_x[i] != bin_y[i]:
        #        count += 1
            
        #return(count)
        
    #simply solution
        return(bin(x^y).count("1"))
    
    