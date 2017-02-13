"""


"""


'''
Created on Jan 23, 2017

@author: fanxueyi
'''

class Solution(object):
    """ 
    def __init__(self):
        self.result=[]
        self.n = 0
        self.k = 0 
    
    #method1 : Time expire limited
    def getPermutation(self, n, k):
        '''
        :type n: int
        :type k: int
        :rtype: str
        '''
        self.n = n
        self.k = k
        n_arr = [i for i in range(1,n+1)]
        comb = ""
        self.helpFun(0, 1, comb, n_arr)
        print(self.result)
        return(self.result[k-1])
        
    def helpFun(self, index, start,comb,n_arr):
        if len(self.result) == self.k:
            return
        if index == self.n:
            self.result.append(comb)
            return
        
        for i in range(len(n_arr)):
            new_comb = comb+str(n_arr[i])
            new_n_arr = n_arr[:i]+n_arr[i+1:]
            self.helpFun(index+1, i+1, new_comb, new_n_arr)
    """
    
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        k = k-1
        n_arr = [i for i in range(1,n+1)]
        comb = ""
        while n > 0:
            n -= 1
            index, k = divmod(k, self.factorial(n))
            comb += str(n_arr[index])
            n_arr.remove(n_arr[index])
        return(comb)
    
    def factorial(self,n):
        res = 1
        for i in range(1,n+1):
            res *= i
        return(res)
        

s=Solution()
print(s.getPermutation(9,171669))



