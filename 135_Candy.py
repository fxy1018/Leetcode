'''
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

Example 1:

Input: [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
             The third child gets 1 candy because it satisfies the above two conditions.


'''


class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        
        这是一个贪心，先正着扫一边，如果序列递增，则糖果数依次加一，如果遇到变小的则设为1。 得到最少的糖果序列 。然后再反向贪心一遍。 最后把两个序列求max  然后相加即可
        """
        candy = [1]
        count = 1
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                count += 1
            else:
                count = 1
            candy.append(count)
        
        count = 1
        candy[-1] = max(candy[-1], count)
        
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                count += 1
            else:
                count = 1
            candy[i] = max(candy[i], count)
        return(sum(candy))
        
