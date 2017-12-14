class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        result = [0 for _ in range(amount+1)]
        result[0] = 1
        for i in range(min(coins), amount+1):
            methods = []
            for c in coins:
                if i-c >=0 and result[i-c] != 0:
                    methods.append(result[i-c])
            if methods:
                result[i] = min(methods)+1
            else:
                result[i] = 0
            
        return(result[-1]-1)
