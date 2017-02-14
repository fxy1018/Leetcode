"""

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in ZigZag-order.
Given a matrix:

[
  [1, 2,  3,  4],
  [5, 6,  7,  8],
  [9,10, 11, 12]
]
return [1, 2, 5, 9, 6, 3, 4, 7, 10, 11, 8, 12]


"""
'''
Created on Feb 14, 2017

@author: fanxueyi
'''


class Solution:
    # @param: a matrix of integers
    # @return: a list of integers
    def printZMatrix(self, matrix):
        # write your code here
        if not matrix:
            return([])
        m = len(matrix)
        n = len(matrix[0]) 
        res = [matrix[0][0]]
        
        if m < 2 :
            return(matrix[0])
        if n < 2:
            for i in range(1, m):
                res.append(matrix[i][n-1])
            return(res)
        
        p1, p2 = [0, 1], [1, 0]
        count = 0
        while p1 != p2:
            #print(p1,p2)
            if count % 2 == 1: 
                dummy_p2 = p2[:]
                while dummy_p2 != p1:
                    res.append(matrix[dummy_p2[0]][dummy_p2[1]])
                    dummy_p2[0] -= 1
                    dummy_p2[1] += 1
                res.append(matrix[p1[0]][p1[1]])
                
            else:
                dummy_p1 = p1[:]
                while dummy_p1 != p2:
                    res.append(matrix[dummy_p1[0]][dummy_p1[1]])
                    dummy_p1[0] += 1
                    dummy_p1[1] -= 1
                res.append(matrix[p2[0]][p2[1]])
           
            if p1[1] != n-1:
                print("first", p1)
                p1[1] += 1
                print(p1)
            else:
                p1[0] += 1
                
            if p2[0] != m-1:
                p2[0] += 1
            else:
                p2[1] += 1
            count += 1
        res.append(matrix[p1[0]][p1[1]])
        return(res)
            
            
s= Solution()
print(s.printZMatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))