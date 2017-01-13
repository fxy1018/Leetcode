"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).


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
        if len(prices) < 2 :
            return 0
        
        maxPro = 0
        for i in range(1,len(prices)):
            tmpPro = prices[i]-prices[i-1]
            if (tmpPro > 0):
                maxPro += tmpPro 
                
        return(maxPro)