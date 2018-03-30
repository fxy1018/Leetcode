'''

Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.
'''

Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.

将整型数组的转化为字符串数组，用 std::sort 对字符串数组排序，使得排序后元素直接连接成为最大值整数。

使用默认的比较函数排序，会得到不一定是最大值，例如 {360, 36} 排序后得到的是 36036 ，明显不是小于 36360。解决这个问题，就是重写比较函数，使得排序后的两个元素连接成为较大的整数即可，很简洁。

'''
#python2
class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        numStr = [str(n) for n in nums]
        numStr = sorted(numStr, reverse = True, cmp=lambda x,y: cmp((x+y), (y+x)))

        res = ''.join(numStr)
        
        #remove 0 at the begining
        i= 0
        while res[i]=='0' and i < len(nums)-1:
            i+=1
        
        return(res[i:])
        
 #python3
class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x
        
class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num
