#dp problem
#Given a number of dollars n, and a list of dollar values for m distinct coins, find and print the number of different ways you can make change for  dollars if each coin is available in an infinite quantity.

#!/bin/python3

import sys

def make_change(coins, n):
    results = [0 for _ in range(n + 1)]
    results[0] = 1
    for coin in coins:
        for i in range(coin, n + 1):
            results[i] += results[i - coin]
    return results[n]
    

n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
coins = [int(coins_temp) for coins_temp in input().strip().split(' ')]
print(make_change(coins, n))
