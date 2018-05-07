'''
Given some intervals, ask how many are covered most, if there are multiple, output the smallest number.

 Notice
the number of the interval is not more than 10^5.
the left and right endpoints of the interval are greater than 0 not more than 10^5.
Have you met this question in a real interview? 
Example
Given intervals = [(1,7),(2,8)], return 2.

Explanation:
2 is covered 2 times, and is the number of 2 times the smallest number.
Given intervals = [(1,3),(2,3),(3,4)], return 3.

Explanation:
3 is covered 3 times.
'''

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    """
    @param intervals: The intervals
    @return: The answer
    """
    def digitalCoverage(self, intervals):
        # Write your code here
        intervals = sorted(intervals, key=lambda x: (x.start, x.end))
        heap = []
        heapq.heappush(heap, intervals[0].end)
        res = intervals[0].start
        maxSize = 1
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval.start <= heap[0]:
                heapq.heappush(heap, interval.end)
                if len(heap) > maxSize:
                    maxSize = len(heap)
                    res = interval.start
            else:
                heapq.heappop(heap)
                heapq.heappush(heap, interval.end)
        return(res)
                
            
