"""

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]


"""


'''
Created on Jan 23, 2017

@author: fanxueyi
'''

class Solution(object):
    def __init__(self):
        self.result = []
        self.k = 0
        self.n = 0
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.k = k
        self.n = n
        comb = []
        self.helpFun(0, 1, comb)
        return(self.result)
        
    def helpFun(self,index,start, comb):
        if index == self.k:
            self.result.append(comb)
            return
        
        #if you k is 5 but you array is only [1, 2, 3], that means you cannot find a combination of 5 numbers b/c you only have 3 number. Therefore in this case I will return my code.
        if self.k-index > self.n-start+1:
            return
        
        for i in range(start,self.n+1):
            new_comb = comb+[i]
            self.helpFun(index+1, i+1, new_comb)




s=Solution()

print(s.combine(5,3))

