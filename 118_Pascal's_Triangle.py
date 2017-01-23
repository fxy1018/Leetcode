"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]


"""

'''
Created on Jan 18, 2017

@author: fanxueyi
'''

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return([])
        out =[[1]]
        for i in range(1,numRows):
            #deep copy
            tmp = out[i-1][:]
            tmp.insert(0,0)
            tmp.append(0)
            arr = []
            for j in range(len(tmp)-1):
                arr.append(tmp[j]+tmp[j+1])
            out.append(arr)
        return(out)
                
            