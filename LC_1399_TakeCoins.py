'''
There aren coins in a row, each time you want to take a coin from the left or the right side. Take a total of k times to write an algorithm to maximize the value of coins.

 Notice

1 <= k <= n <= 100000。
The value of the coin is not greater than 10000。
Have you met this question in a real interview? Yes
Example
Given list = [5,4,3,2,1], k = 2, return 9.

Explanation:
Take two coins from the left.
Given list = [5,4,3,2,1,6], k = 3, return 15.

Explanation:
Take two coins from the left and one from the right.

'''

class Solution:
    """
    @param list: The coins
    @param k: The k
    @return: The answer
    """
    def takeCoins(self, list, k):
        # Write your code here
        memo = [[0] * len(list) for _ in range(len(list))]
        return(self.helpFun(0, len(list)-1, list, k, memo))
        
    def helpFun(self, i, j, list, k, memo):
        if k == 0:
            return(memo[i][j])
        if i == j :
            memo[i][j] = list[i]
            return(list[i])
        if memo[i][j] != 0:
            return(memo[i][j])
        
        left = list[i] + self.helpFun(i+1, j, list, k-1, memo)
        right = list[j] + self.helpFun(i, j-1, list, k-1, memo)
        memo[i][j] = max(left, right)
        
        return(memo[i][j])
 
 class Solution:
    """
    @param list: The coins
    @param k: The k
    @return: The answer
    """
    def takeCoins(self, list, k):
        # Write your code here
        print(len(list))
        if k >= len(list):
            return(sum(list))
        #find subarray with window (len(list)-k) which has the minimun sum
        left = 0
        right = len(list)-k
        pre = res = sum(list[left : right])
        for i in range(right, len(list)):
            pre = pre + list[i] - list[left]
            res = min(pre, res)
            left += 1
        return(sum(list)-res)
        
