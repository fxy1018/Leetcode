"""

给定数组 arr ，arr 中所有的值都为正数且不重复。
每个代表一种面货币，种面值的货币可以使用任意张 ，
再给定一个整数aim代表要找的钱数 ，求换钱有多少种方法。

"""

class Solution(object):
    def coins1(self, arr, aim):
        if not arr or aim < 0:
            return(0)
        return self.process1(arr, 0, aim)
    
    def process1(self, arr, index, aim):
        res = 0
        if index == len(arr):
            if aim == 0:
                res = 1
            else:
                res = 0
        else:
            i = 0
            while arr[index] * i <= aim:
                res += self.process1(arr, index+1, aim-arr[index]*i)
                i += 1  
        return(res)
    
    
            
    