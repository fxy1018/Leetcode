'''
Created on Feb 1, 2017

@author: fanxueyi

'''

"""

思路: 一道很明显的动态规划的题目. 每个房子有三种染色方案, 那么如果当前房子染红色的话, 最小代价将是上一个房子的绿色和蓝色的最小代价+当前房子染红色的代价. 对另外两种颜色也是如此. 因此动态转移方程为: 

             dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i-1][0];

             dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i-1][1];

             dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i-1][2];
             
"""


class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        #0: red; 1:blue; 2:green
        
        n = len(costs)
        cost_total = [[0]*3 for i in range(n+1)]
        if n==0:
            return(0)
        
        for i in range(1,n+1):
            cost_total[i][0] = min(cost_total[i-1][1],cost_total[i-1][2])+costs[i-1][0]
            cost_total[i][1] = min(cost_total[i-1][0],cost_total[i-1][2])+costs[i-1][1]
            cost_total[i][2] = min(cost_total[i-1][0],cost_total[i-1][1])+costs[i-1][2]
            
        return(min(cost_total[n][0], cost_total[n][1], cost_total[n][2]))    
        
        

