'''
There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.

 Notice
All costs are positive integers.

Example
Given n = 3, k = 3, costs = [[14,2,11],[11,14,5],[14,3,10]] return 10

house 0 is color 2, house 1 is color 3, house 2 is color 2, 2 + 5 + 3 = 10

Challenge 
Could you solve it in O(nk)?

'''

class Solution:
    """
    @param costs: n x k cost matrix
    @return: an integer, the minimum cost to paint all houses
    """
   #time limit exceeded
    def minCostII(self, costs):
        # write your code here
        if not costs:
            return(0)
            
        house = len(costs)
        color = len(costs[0])
        
        #create dp 
        dp = [[0] * color for _ in range(house)]
        dp[0] = costs[0]
        
        for i in range(1, house):
            for j in range(color):
                last = []
                for z in range(color):
                    if z != j:
                        last.append(dp[i-1][z])
                dp[i][j] = min(last) + costs[i][j]
        return(min(dp[-1]))
class Solution:
    """
    @param costs: n x k cost matrix
    @return: an integer, the minimum cost to paint all houses
    """
    #similar strategy as paint house 1 but use two variables to record the last two mins for each row
    def minCostII(self, costs):
        # write your code here
        if not costs:
            return(0)
            
        house = len(costs)
        color = len(costs[0])
        
        #create dp 
        dp = [[0] * color for _ in range(house)]
        dp[0] = costs[0]
        if costs[0][0] <= costs[0][1]:
            min1 = 0
            min2 = 1
        else:
            min1 = 1
            min2 = 0
            
        for i in range(2, color):
            if costs[0][i] < costs[0][min1]:
                min2 = min1
                min1 = i
                
            elif costs[0][i] == costs[0][min1] or costs[0][i] < costs[0][min2]:
                min2 = i
            
        for i in range(1, house):
            last1 = -1
            last2 = -1
            for j in range(color):
                if j == min1:
                    dp[i][j] = dp[i-1][min2] + costs[i][j]
                else:
                    dp[i][j] = dp[i-1][min1] + costs[i][j]
                
                if last1 == -1:
                    last1 = j
                else:
                    if dp[i][j] < dp[i][last1]:
                        last2 = last1
                        last1 = j
                    elif dp[i][j] == dp[i][last1]:
                        last2 = j
                    elif last2 == -1 or dp[i][j] < dp[i][last2]:
                        last2 = j
            min1 = last1
            min2 = last2
                
        return(min(dp[-1]))
       
       
