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

