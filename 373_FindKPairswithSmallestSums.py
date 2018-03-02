'''
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u,v) which consists of one element from the first array and one element from the second array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:
Given nums1 = [1,7,11], nums2 = [2,4,6],  k = 3

Return: [1,2],[1,4],[1,6]

The first 3 pairs are returned from the sequence:
[1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:
Given nums1 = [1,1,2], nums2 = [1,2,3],  k = 2

Return: [1,1],[1,1]

The first 2 pairs are returned from the sequence:
[1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
Example 3:
Given nums1 = [1,2], nums2 = [3],  k = 3 

Return: [1,3],[2,3]

All possible pairs are returned from the sequence:
[1,3],[2,3]

'''

import heapq
class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        #use max heap with size K to get smallest K
        l1 = len(nums1)
        l2 = len(nums2)
        heap = []
        
        for i in range(l1):
            for j in range(l2):
                tmpSum = nums1[i] + nums2[j]
                if len(heap) < k:
                    heapq.heappush(heap, [-tmpSum, nums1[i],nums2[j]])
                else:
                    if tmpSum <= -heap[0][0]:
                        heapq.heappop(heap)
                        heapq.heappush(heap, [-tmpSum, nums1[i],nums2[j]])
        out = []
        while heap:
            tmpSum, num1, num2 = heapq.heappop(heap)
            out.append([num1,num2])
        return(out[::-1])
