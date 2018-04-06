"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Refer: http://liangjiabin.com/blog/2015/04/leetcode-best-time-to-buy-and-sell-stock.html
"""

'''
Created on Jan 13, 2017

@author: fanxueyi
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        
        if len(prices) <2:
            return 0
        
        prePro, postPro = [0]*len(prices), [0]*len(prices)
        curMin = prices[0]
        for i in range(1, len(prices)):
            curMin = min(prices[i], curMin)
            prePro[i] = max(prePro[i-1], prices[i]-curMin)
        
        
        
        curMax = prices[len(prices)-1]
        for j in range(-1, -len(prices)-1,-1):
            curMax = max(prices[j],curMax)
            postPro[j] = max(postPro[j+1], curMax-prices[j])
    
        
        maxPro = 0
        for i in range(len(prices)):
            maxPro= max(maxPro, prePro[i]+postPro[i])
        
   
        return(maxPro)
    
solution = Solution()
print(solution.maxProfit([1,2,4]))


"""

需要用动态规划Dynamic Programming来解，而这里我们需要两个递推公式来分别更新两个变量local和global，参见网友Code Ganker的博客，我们其实可以求至少k次交易的最大利润，找到通解后可以设定 k = 2，即为本题的解答。我们定义local[i][j]为在到达第i天时最多可进行j次交易并且最后一次交易在最后一天卖出的最大利润，此为局部最优。然后我们定义global[i][j]为在到达第i天时最多可进行j次交易的最大利润，此为全局最优。它们的递推式为：

local[i][j] = max(global[i - 1][j - 1] + max(diff, 0), local[i - 1][j] + diff)

global[i][j] = max(local[i][j], global[i - 1][j])

其中局部最优值是比较前一天并少交易一次的全局最优加上大于0的差值，和前一天的局部最优加上差值中取较大值，而全局最优比较局部最优和前一天的全局最优。
"""
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
                # write your code here
        if not prices:
            return(0)
            
        l = [[0] * (3) for _ in range(len(prices))]
        g = [[0] * (3) for _ in range(len(prices))]
        
        for i in range(1, len(prices)):
            for j in range(1, 3):
                diff = prices[i] - prices[i-1]
                l[i][j] = max(g[i-1][j-1] + max(diff, 0), l[i-1][j] + diff)
                g[i][j] = max(l[i][j], g[i-1][j])
        
        return(g[-1][-1])





