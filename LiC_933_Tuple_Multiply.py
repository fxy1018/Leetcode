'''
Given a string tuple, which represents a series of arrays such as "(1,2,3),(4,5,6),(7,8,9)". Then given a number n, which means that we need to find the product of all the nth element in each array.

 Notice
We guarantee that the absolute value of answer does not exceed 10^18.
The element of array described by string is in the int range.

Example
Given tuple = "(1,2,3),(4,5,6),(7,8,9)", n = 2, return 80.

Explanation:
The second elemnts of each array are 2, 5, 8, so the product is 80. 
Given tuple = "(1,2,3),(4,5,6),(7,8,9)", n = 3, return 162.

Explanation:
The third elements of each array are 3, 6, 9, so the product is 162.

'''

class Solution:
    """
    @param tuple: the tuple string
    @param n: an integer
    @return: the product of all the nth element in each array
    """
    def tupleMultiply(self, tuple, n):
        # Write your code here
        stack = []
        i = 0
        l = len(tuple)
        arr = []
        currN = 0
        res = 1 
        while i < l :
            c = tuple[i]
            if c in ",(":
                i += 1
            elif c in "-0123456789":
                if c == "-":
                    sign = -1
                    i += 1
                else:
                    sign = 1
                while tuple[i] in "0123456789":
                    currN = 10*currN + int(tuple[i])
                    i += 1
                stack.append(sign*currN)
                currN = 0
            elif c == ")":
                tmp = []
                while stack:
                    tmp.append(stack.pop())
                res *= tmp[len(tmp)-n]
                i+=1
        return(res)
                    
                
                
