'''
A n*m matrix represents an array of computers, and give a list which represents the coordinate of the broken computer. Now we start with (0,0) and repair the computer. There are some request:
1. You have to fix all the broken computers in the current line to get to the next line.
2. If you are going to the next line, the mechanic must first return to the far left or right of the line.
Find the minimum access distance.

 Notice
The size of the given matrix is n x m, n <= 200, m <= 200.
num is the number of broken computer, num <= 1000.
After fixing the last computer, you need to return to the far left or right of the last line.
Have you met this question in a real interview? 
Example
Given n = 3, m = 10, List = [[0,0],[0,9],[1,7]], return 15.

Explanation:

Starting from (0,0), fix 0, then go to (0,9) to fix 1 and go from (0,9) to next line (1,9), then go to (1,7) to fix 3, then go back to (1,9) and go to (2,9).
Given n = 3, m = 10, List = [[0,3],[1,7],[1,2]], return 17.

Explanation:

Starting from (0,0), go to (0,3) and fix 0, then go back to (0,0) to next line (1,0), and go to (1,2) to fix 2, then go to (1,7) to fix 1, then go to (1,9), and end at (2,9).

'''

class Solution:
    """
    @param n: the rows of matrix
    @param m: the cols of matrix
    @param badcomputers: the bad computers 
    @return: The answer
    """
    def maintenance(self, n, m, badcomputers):
        # Write your code here
        dp = [[0, 0] for i in range(201)]
        matrix = [[0 for i in range(201)] for j in range(201)]
        for node in badcomputers:
            matrix[node.x][node.y] = 1
        for i in range(n):
            most_right = -1
            most_left = -1
            for j in range(m):
                if matrix[i][j] != 0:
                    most_right = max(most_right, j)
                    most_left = max(most_left, m - 1 - j)
            if i == 0:
                if most_right == -1:
                    dp[i][0] = 0
                    dp[i][1] = m - 1
                else:
                    dp[i][0] = 2 * most_right
                    dp[i][1] = m - 1
                continue
            if most_right == -1:
                dp[i][0] = dp[i - 1][0] + 1
                dp[i][1] = dp[i - 1][1] + 1
            else:
                dp[i][0] = min(dp[i - 1][0] + 2 * most_right, dp[i - 1][1] + m - 1) + 1;
                dp[i][1] = min(dp[i - 1][1] + 2 * most_left, dp[i - 1][0] + m - 1) + 1;
        return min(dp[n - 1][0], dp[n - 1][1]);
