"""

Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.


"""

'''
Created on Mar 3, 2017

@author: fanxueyi
'''

'''
Naive Solution

暴力解什么很显然, 可以直接在O(n^2)的时间内进行两两计算, 并且保存最大值, 代码什么的也不说了, 很简单.

Better Solution

对输入的数组, 我们将其中的元素根据最高位的值分为两类, 最高位为0的一类, 最高位为1的一类, 如果两类都不为空, 那么该问题的最终结果一定是从第一类中找一个数和第二类中的一个数进行异或得到的结果.

那么此题就可以优化为, 从两个数列中各取一个数, 求两个数按位异或结果的最大值. 因此, 我们可以设计一个helper函数帮我们处理.

那么, 我们可以根据次高位再将数继续分成两类, 因此, 我们可以得到四个类, arr00, arr01, arr10, arr11. 那么最终的解一定在(arr00, arr11), (arr10, arr01)中; 如果存在空集, 那么最终的解一定在(arr00, arr01), (arr11, arr10)中.

平均时间复杂度分析, 假设O(n)表示helper函数的时间复杂度, 其中n表示传入helper两个数列的总长度. 那么我们有 O(n) = n + 2 * O(n/2), 化简后可得 O(n) = O(n log n) + O(n) = O(n log n)


利用异或的特性, 这题可以有更好的解法. 对于异或运算, 我们有

如果a ^ b = c, 那么a ^ c = b.

根据这个定理, 我们从最高位开始找, 我们先将所有数的最高位存到一个Set中. 然后, 我们假设最终答案的最高位为1, 将数列中所有数的最高位和1进行异或运算, 异或得到的结果仍然在Set中, 那么说明最终答案的最高位一定为1, (由定理可得1 ^ x = b <==> b ^ x = 1, 对与数x, 一定存在一个数b, 使得x ^ b = 1), 否则最高位的答案一定为0.

假设我们已经知道最终答案的最高k位为prefix, 我们先将数列中所有数的最高k+1位存入Set中. 然后, 我们假设下一位的值为1, 将数列中所有数的最高k+1位与prefix*2 + 1进行异或运算, 如果异或得到的结果仍然在Set中, 那么说明最终答案的第k+1位一定为1, 否则, 最高位的答案一定为0.

因为x ^ (prefix*2+1) = b　<==> x ^ b = prefix*2+1, 即对于数x, 一定存在一个数b, 使得他们异或的结果为prefix*2+1.

因此, 我们可以对最终答案的32位进行依次判断, 最终得到异或的最大值.

该算法的时间复杂度为O(32n) = O(n).

'''

#http://hankerzheng.com/blog/LeetCode-Maximum-XOR-of-Two-Numbers-in-an-Array

class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.nums = nums
        return(self.helper(nums, [], 32))
    
    def partition(self, nums, index):  
        mask = 1 << index
        arr0, arr1 = [], []
        for num in nums:
            if num & mask :
                arr1.append(num)
            else:
                arr0.append(num)
        return(arr0, arr1)
    
    def helper(self, arr0, arr1, index):
        if not arr0 and not arr1:
            return(0)
        if not arr0 or not arr1:
            if index == 0:
                return(0)
            
            arr = arr0 if arr0 else arr1
            arr0, arr1 = self.partition(arr, index-1)
            return(self.helper(arr0, arr1, index-1))
        
        if index == 0:
            return arr0[0] ^ arr1[0]
        arr00, arr01 = self.partition(arr0, index-1)
        arr10, arr11 = self.partition(arr1, index-1)
        
        if arr00 and arr11 or arr10 and arr01:
            return(max(self.helper(arr00, arr11, index-1), self.helper(arr10, arr01, index-1)))
        else:
            return(max(self.helper(arr01, arr11, index - 1), self.helper(arr00, arr10, index - 1)))



