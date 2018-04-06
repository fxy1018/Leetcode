"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
需要用动态规划Dynamic Programming来解，而这里我们需要两个递推公式来分别更新两个变量local和global，参见网友Code Ganker的博客，我们其实可以求至少k次交易的最大利润，找到通解后可以设定 k = 2，即为本题的解答。我们定义local[i][j]为在到达第i天时最多可进行j次交易并且最后一次交易在最后一天卖出的最大利润，此为局部最优。然后我们定义global[i][j]为在到达第i天时最多可进行j次交易的最大利润，此为全局最优。它们的递推式为：

local[i][j] = max(global[i - 1][j - 1] + max(diff, 0), local[i - 1][j] + diff)

global[i][j] = max(local[i][j], global[i - 1][j])

其中局部最优值是比较前一天并少交易一次的全局最优加上大于0的差值，和前一天的局部最优加上差值中取较大值，而全局最优比较局部最优和前一天的全局最优。

"""
class Solution:
  #memory error
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return(0)
            
        l = [[0] * (k+1) for _ in range(len(prices))]
        g = [[0] * (k+1) for _ in range(len(prices))]
        
        for i in range(1, len(prices)):
            for j in range(1, k+1):
                diff = prices[i] - prices[i-1]
                l[i][j] = max(g[i-1][j-1] + max(diff, 0), l[i-1][j] + diff)
                g[i][j] = max(l[i][j], g[i-1][j])
        
        return(g[-1][-1])
        
      #compress space, 2D matrix -> array , memory error
          def maxProfit(self, K, prices):
        # write your code here
        if not prices:
            return(0)
            
        l = [0] * (K+1) 
        g = [0] * (K+1) 
        
        for i in range(1, len(prices)):
            for j in range(K, 0, -1):
                diff = prices[i] - prices[i-1]
                l[j] = max(g[j-1] + max(diff, 0), l[j] + diff)
                g[j] = max(l[j], g[j])
        
        return(g[-1])
        
        
        
   def solution3(K, prices)
       if not prices:
            return(0)
         
        if K >= len(prices)//2:
            return(sum(x-y for x,y in zip(prices[1:], prices[:-1]) if x>y))
        
        l = [0] * (K+1) 
        g = [0] * (K+1) 
        
        for i in range(0, len(prices)-1):
            diff = prices[i+1] - prices[i]
            for j in range(K, 0, -1):
                l[j] = max(g[j-1] + max(diff, 0), l[j] + diff)
                g[j] = max(l[j], g[j])
        
        return(g[-1])

      #modified relationship:
      
      #local[i][j] = max(global[i - 1][j - 1], local[i - 1][j]) + diff

      #global[i][j] = max(local[i][j], global[i - 1][j])
