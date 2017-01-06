#Given two sparse matrices A and B, return the result of AB.

#You may assume that A's column number is equal to B's row number.

'''
Created on Jan 5, 2017

@author: fanxueyi
'''

class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if not A or not B: 
            return None
        
        m = len(A)
        n = len(A[0])
        l = len(B[0])
        if len(B) != n :
            raise Exception("A's column number must be equal to B's row number.")
        C = [[0 for i in range(l)] for j in range(m)]
        B_hash = {}
        for k, row in enumerate(B):
            B_hash[k] = {}
            for j, eleB in enumerate(row):
                if eleB:
                    B_hash[k][j] = eleB
        for i, row in enumerate(A):
            for k, eleA in enumerate(row):
                if eleA:
                    #When using items() method, the iteration needs to be completed 
                    #and stored in-memory before for loop can begin iterating. 
                    #The prefered way is to use iteritems. 
                    for j, eleB in B_hash[k].iteritems():
                        C[i][j] += eleA * eleB
                        
        return(C)