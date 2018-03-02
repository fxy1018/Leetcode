'''

Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note: 
You may assume k is always valid, 1 ≤ k ≤ n2.

'''

import heapq
class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        #use maxheap
        heap = []
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if len(heap) < k:
                    heapq.heappush(heap, -matrix[i][j])
                
                else:
                    if matrix[i][j] <= -heap[0]:
                        heapq.heappop(heap)
                        heapq.heappush(heap, -matrix[i][j])
        return(-heap[0])
