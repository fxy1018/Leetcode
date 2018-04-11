'''
Given a non-repeating prime array arr, and each prime number is used at most once, find all the product without duplicate and sort them from small to large.

 Notice
2 <= |arr| <= 9
2 <= arr[i] <= 23

Example
Given arr = [2,3], return [6].

Explanation:
2 * 3 = 6.
Gven arr = [2,3,5], return [6,10,15,30].

Explanation:
2 * 3 = 6, 2 * 5 = 10, 3 * 5 = 15, 2 * 3 *5 = 30。
'''

class Solution:
    """
    @param arr: The prime array
    @return: Return the array of all of prime product
    """
    def getPrimeProduct(self, arr):
        # Write your code here
        res = []
        l = len(arr)
        arr = sorted(arr)
        
        for i in range(l-1):
            curr = arr[i]
            self._helpFun(arr, res, i, curr, l)
        return(sorted(res))
        
    def _helpFun(self, arr, res, index, curr, l):
        if index == l:
            return
        for i in range(index+1, l):
            curr *= arr[i]
            if int(curr) not in res:
                res.append(int(curr))
            self._helpFun(arr, res, i, curr, l)
            curr /= arr[i]
        
