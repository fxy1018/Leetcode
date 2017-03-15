"""

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.

"""

'''
Created on Mar 14, 2017

@author: fanxueyi
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        
        curMin = prices[0]
        maxPro = 0
        
        for i in range(len(prices)):
            curMin = min(prices[i], curMin)
            maxPro = max(prices[i]-curMin, maxPro)
        
        return(maxPro)
    
    
'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

'''

class Solution2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """     
        if len(prices) < 2 :
            return 0
        
        maxPro = 0
#         for i in range(1,len(prices)):
#             tmpPro = prices[i]-prices[i-1]
#             if (tmpPro > 0):
#                 maxPro += tmpPro 
        
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                maxPro += prices[i] - prices[i-1]
        return(maxPro)
    
    
'''

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

允许两次买卖，但同一时间只允许持有一支股票。也就意味着这两次买卖在时间跨度上不能有重叠（当然第一次的卖出时间和第二次的买入时间可以是同一天）。既然不能有重叠可以将整个序列以任意坐标i为分割点，分割成两部分：

prices[0:n-1] => prices[0:i] + prices[i:n-1]

对于这个特定分割来说，最大收益为两段的最大收益之和。每一段的最大收益当然可以用I的解法来做。而III的解一定是对所有0<=i<=n-1的分割的最大收益中取一个最大值。为了增加计算效率，考虑采用dp来做bookkeeping。目标是对每个坐标i：

1. 计算A[0:i]的收益最大值：用minPrice记录i左边的最低价格，用maxLeftProfit记录左侧最大收益
2. 计算A[i:n-1]的收益最大值：用maxPrices记录i右边的最高价格，用maxRightProfit记录右侧最大收益。
3. 最后这两个收益之和便是以i为分割的最大收益。将序列从左向右扫一遍可以获取1，从右向左扫一遍可以获取2。相加后取最大值即为答案。
'''
    
    
    
class Solution3(object):
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
    def maxProfit2(self, prices):
        if len(prices) < 2:
            return(0)
        
        minPrice = prices[0]
        maxLeftProfit = 0
        left = [0]
        for i in range(1,len(prices)):
            minPrice = min(minPrice, prices[i])
            maxLeftProfit = max(maxLeftProfit, prices[i]-minPrice)
            left.append(maxLeftProfit)
        
        maxPrice = prices[-1]
        maxRightProfit = res =0
        for i in range(len(prices)-1, -1, -1):
            maxPrice = max(maxPrice, prices[i])
            maxRightProfit = max(maxRightProfit, maxPrice-prices[i])
            res = max(res, maxRightProfit+left[i])
        return(res)
    
'''
188. Best Time to Buy and Sell Stock IV
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

'''

class Solution4(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
            
    
    