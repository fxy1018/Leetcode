'''
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.

Example
Example 1:

Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: True
Explanation:
1234
5123
9512

In the above grid, the diagonals are "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]", and in each diagonal all elements are the same, so the answer is True.


Example 2:

Input: matrix = [[1,2],[2,2]]
Output: False
Explanation:
The diagonal "[1, 2]" has different elements.

'''
class Solution:
    """
    @param matrix: the given matrix
    @return: True if and only if the matrix is Toeplitz
    """
    def isToeplitzMatrix(self, matrix):
        # Write your code here
        #two coordinates (r1, c1) and (r2, c2)
        #It turns out two coordinates are on the same diagonal if and only if r1 - c1 == r2 - c2.
        row = len(matrix)
        col = len(matrix[0])
        group = {}
        for i in range(row):
            for j in range(col):
                val = matrix[i][j]
                if i-j not in group:
                    group[i-j] = val
                elif group[i-j] != val:
                    return(False)
        return(True)
        
