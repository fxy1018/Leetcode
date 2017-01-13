"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

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
        if len(prices) < 2:
            return 0
        
        curMin = prices[0]
        maxPro = 0
        
        for i in range(len(prices)):
            curMin = min(prices[i], curMin)
            maxPro = max(prices[i]-curMin, maxPro)
        
        return(maxPro)