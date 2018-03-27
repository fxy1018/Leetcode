"""

Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?

"""

'''
Created on Jan 18, 2017

@author: fanxueyi
'''
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        #method1: space O(k^2)
        out =[[1]]
        for i in range(1,rowIndex+1):
            #deep copy
            tmp = out[i-1][:]
            tmp.insert(0,0)
            tmp.append(0)
            arr = []
            for j in range(len(tmp)-1):
                arr.append(tmp[j]+tmp[j+1])
            out.append(arr)
        return(out[-1])
        
        #method2: space O(k)
        out =[1]
        for i in range(1,rowIndex+1):
            #deep copy
            out.insert(0,0)
            out.append(0)
            arr = []
            for j in range(len(out)-1):
                out[j] = (out[j]+out[j+1])
            out.pop()
        return(out)
class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return([1])
        pre = [1]
        for i in range(1, rowIndex+1):
            l = len(pre)
            tmp = []
            for j in range(l+1):
                if j == 0 or j ==l:
                    tmp.append(1)
                else:
                    tmp.append(pre[j] + pre[j-1])
            pre = tmp
        return(pre)
