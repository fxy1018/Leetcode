"""
LC217:
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

LC219:
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

LC220:
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

"""

'''
Created on Jan 13, 2017

@author: fanxueyi
'''
class Solution217(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        return(len(nums) != len(set(nums)))
    
    def containsDuplicate2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numHash = {}
        for n in nums:
            numHash[n] = numHash.get(n, 0) + 1
            if numHash[n] ==2:
                return(True)
        return(False)    

class Solution219(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums:
            return(False)
        
        dic = {}
        
        for i in range(len(nums)):
            if nums[i] in dic:
                if abs(dic[nums[i]] - i) <= k:
                    return(True)
            dic[nums[i]] = i
        
        return(False)
    
 class Solution219_2(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        numHash = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in numHash and i-numHash[num] <=k:
                    return(True)
            numHash[num] = i
            
        return(False)

    
    #这里有两个限制条件，两个数字的坐标差不能大于k，值差不能大于t。这道题如果用brute force会超时，所以我们只能另辟蹊径。这里我们使用map数据结构来解,用来记录数字和其下标之间的映射。 这里需要两个指针i和j，刚开始i和j都指向0，然后i开始向右走遍历数组，如果i和j之差大于k，且m中有nums[j]，则删除并j加一。这样保证了m中所有的数的下标之差都不大于k，然后我们用map数据结构的lower_bound()函数来找一个特定范围，就是大于或等于nums[i] - t的地方，所有小于这个阈值的数和nums[i]的差的绝对值会大于t (可自行带数检验)。然后检测后面的所有的数字，如果数的差的绝对值小于等于t，则返回true。最后遍历完整个数组返回false。
class Solution220(object):
        
