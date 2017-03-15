"""
given a array and window size k, give the max/min array
when the window slide from left to right

ex:
arr = [4,3,5,4,3,3,6,7], k= 3
return [5,5,5,4,6,7]

"""
'''

Created on Mar 14, 2017

@author: fanxueyi
'''

class Solution(object):
    def getMax(self, arr, k): 
        if arr==None or k < 1 or len(arr) < k:
            return None
        
        res = []      
        helpArr = []
        for i in range(0,len(arr)):
            while helpArr and arr[i] >= arr[helpArr[-1]]:
                helpArr.pop()
            helpArr.append(i)
            if helpArr[0] == i-k:
                helpArr.pop(0)
            if arr[i] < arr[helpArr[-1]]:
                helpArr.append(i)
            if i >= k-1:
                res.append(arr[helpArr[0]])
        return(res)
            
s = Solution()
print(s.getMax([4,3,5,4,3,3,6,7], 3))        