'''


'''

class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #greedy
        '''
        解题思路

刚开始的时候老是想着在扫描数组时，每扫描到一个新的数字都要确定以该数字为开头的一个连续序列。其实根本不需要扫到一个数字就确定一个连续序列，而是可以在扫描数组的过程中，把数字逐一地添加到未完整的连续序列中，动态地往连续序列中添加数据。整个算法过程如下：

维护两个哈希表 frequency 和 tails. frequency 表记录数组中每个数字出现的次数，而 tails 表则记录以某个数字结尾的连续序列的个数，比如 tails[key] 的值为2，表示以数字 key 为结尾的连续序列共有两个。

第一次扫描数组，把数组中每个数字的出现次数记录到 frequency 表中。

第二次扫描数组，对扫描到的每一个数字 num，如果 tails[num - 1] > 0 ，说明存在以 num - 1 为结尾的连续序列，则把数字 num 添加到该连续序列中：tails[num - 1]--; tails[num]++。可能有人会担心 num可能是另一个连续序列的开始数字而不应该加入到 tails[num - 1] 的连续序列中，但是任意以 num 为开始数组的连续序列都可以与 tails[num - 1] 的连续序列合并：比如 [1, 2, 3] 和 [4, 5, 6] 两个连续序列是可以合并成 [1, 2, 3, 4, 5, 6] 这个大的连续序列的，这对于结果是没有影响的；如果 tails[num - 1] == 0 ，此时我们就需要以 num 为开始数字建立一个新的连续序列。而一个连续序列至少包含 3 个数字，因此还要检查 num + 1 和 num + 2 这两个数字是否存在，如果不存在，则直接 return false ，否则，新建以 num + 2 数字为结尾的连续序列。

如果上述过程能进行到最后，说明所有连续序列都能够找出来，则直接 return true。
        '''
        
        frequency =collections.Counter()
        tails = collections.Counter()
        for n in nums:
            frequency[n] = frequency.get(n,0)+1 
        for num in nums:
            if frequency[num] == 0:
                continue
            elif tails[num-1] >0:
                tails[num-1] -=1
                tails[num] = tails.get(num,0) + 1
            elif frequency[num+1] >0 and frequency[num+2]>0:
                tails[num+2] +=1
                frequency[num+1] -=1
                frequency[num+2] -=1
            else:
                return(False)
            frequency[num] -=1
        return(True)
