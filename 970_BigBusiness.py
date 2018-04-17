'''
Given two arrays a and b. a[i] stands for the royalties of the film i, b[i] represents the money that the movie i can sell, now we have principal k, find how much money can be earned in the end.(Each movie only needs to be bought once and can only be sold once.)

 Notice
All the input does not exceed 100000
The size of array does not exceed 10000.

Example
Given a = [3,1,5], b = [4,3,100], k = 1，return 4.

Explanation:
Buy the second video first, then sell it, buy the first video, sell it again, and finally the principal becomes 4.
Given a = [3,1,5], b = [4,3,100], k = 10，return 108。

Explanation:
Buy all the videos, sell them, and finally the principal becomes 108.
'''

#math + array, greedy
class Solution:
    """
    @param a: The cost of the film
    @param b: The price of the selling of the film
    @param k: The principal
    @return: The answer
    """
    def bigBusiness(self, a, b, k):
        # Write your code here
        filmHash = {}
        for i in range(len(a)):
            if a[i] < b[i]:
                filmHash[a[i]] = filmHash.get(a[i], 0) + (b[i]-a[i])
    
        keys = sorted(filmHash.keys())
        for key in keys:
            if k>=key:
                k += filmHash[key]
        return(k)
