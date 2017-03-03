"""

The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

"""

'''
Created on Mar 2, 2017

@author: fanxueyi
'''
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return("1")
        else:
            return(self.read(self.countAndSay(n-1)))
            
    def read(self, num):
        p = num[0]
        count = 0
        out = ""
        for i in num:
            if i == p:
                count += 1
            else:
                out += str(count) + p
                count = 1
                p = i
        out += str(count) + p
        return(out)
        
#use iteration

class Solution2(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return("1")
        curr_num = 1
        for i in range(1, n):
            curr_num = self.readNum(curr_num)
        
        return(str(curr_num))
    
    def readNum(self, num):
        num = str(num)
        count = 0
        preChar = num[0]
        out = ""
        for c in num:
            if c == preChar:
                count += 1
            else:
                out += str(count) + str(preChar)
                preChar = c
                count = 1
        out += str(count) + str(preChar)
        return(int(out))
            