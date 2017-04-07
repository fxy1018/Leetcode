"""
给定整数 N，返回斐波那契数列的第 N项

"""


'''
Created on Mar 22, 2017

@author: fanxueyi
'''


class FibonacciProblem(object):
    def f1(self, n):
        if n< 1:
            return 0
        if n == 1 or n == 2:
            return 1
        return(self.f1(n-1) + self.f2(n-2))

    def f2(self, n):
        if n < 1:
            return 0
        if n == 1 or n ==2 :
            return 1
        
        val1 = 1
        val2 = 1
        for i in range(3, n+1):
            tmp = val1 + val2
            val1 = val2
            val2 = tmp
            
        return(val2)
s = FibonacciProblem()
print(s.f2(5))



class countCows(object):
    def c1(self,n):
        if n < 1 :
            return 0
        if n < 4:
            return n
        return(self.c1(n-1) + self.c1(n-3))
    
    def c2(self, n):
        if n < 1 :
            return 0
        if n == 1 or n==2 or n==3:
            return n
        val1 = 1
        val2 = 2
        val3 = 3
        for i in range(4, n+1):
            tmp1 = val1 + val3
            val1 = val2
            val2 = val3
            val3 = tmp
        return(val3)
