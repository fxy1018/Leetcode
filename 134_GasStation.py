'''
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.

Note:

If there exists a solution, it is guaranteed to be unique.
Both input arrays are non-empty and have the same length.
Each element in the input arrays is a non-negative integer.
Example 1:

Input: 
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

Output: 3

Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.
Example 2:

Input: 
gas  = [2,3,4]
cost = [3,4,3]

Output: -1

Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.


解决方案的关键就是题目的限制条件“本题目只有唯一一个解”。

由于只有唯一解 i ，则以下性质：

性质1. 任何 j ( 0<= j < i) 都不可能到达 i 。

性质2. 任何 k (i <= i < n) ，i 都可以到达。

所以，从左往右扫，当遇到第一个i, 满足 sum[i,j] (i <= j < n) 均大于等于0，那么 i 便是题目的解。

若对每一个元素都检查 sum[i,j] ，那么耗时为 O(n*n) 。这里借助 性质1 优化查找。

假设 sum[i1, j] (i1<= j < t2) 都大于等于 0 ，当 j = t2 时，sum[i1, j] 小于 0 ，那么 i1 不是解，根据性质1，i1~ t2 都不是解。可以从 t2+1 开始继续扫。



'''





class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        netGas= [gas[i]-cost[i] for i in range(len(gas))]
        if sum(netGas) < 0:
            return(-1)
        
        rem = 0
        res = 0
        for i in range(len(gas)):
            rem += netGas[i]
            if rem < 0:
                rem = 0
                res = i + 1
        return(res)
        
