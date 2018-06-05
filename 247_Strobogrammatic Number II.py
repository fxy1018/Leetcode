'''
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
Find all strobogrammatic numbers that are of length = n.

Example
Given n = 2, return ["11","69","88","96"].

'''

class Solution:
    """
    @param n: the length of strobogrammatic number
    @return: All strobogrammatic numbers
    """
    def findStrobogrammatic(self, n):
        # write your code here
        numHash = {'0':'0', '1':'1', '8':'8', '6':'9', '9':'6'}
        keys = sorted(numHash.keys())
        if n == 0:
            return([""])

        if n%2==0:
            mid = ['']
        else:
            mid = ['0','1','8']
        
        res = self.helpFun(n//2, numHash)
        out = []
        for r in res:
            for m in mid:
                tmp = r + m + self.mirror(r)
                out.append(tmp)
        return(out)
    
    def helpFun(self, n, keys):
        if n == 0:
            return([""])
        res = ['1','8','6','9']
        for i in range(1, n):
            tmp = []
            for r in res:
                for key in keys:
                    tmp.append(r+key)
            res = tmp
        return(res)        

    def mirror(self, num):
        # write your code here
        if not num:
            return("")
        numHash= {'6':'9', '9':'6', '8':'8', '1':'1', '0':'0'}
        rotateNum = ""
        for n in num:
            rotateNum = numHash[n] + rotateNum
        return(rotateNum)
