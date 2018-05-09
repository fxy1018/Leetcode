'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

'''

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        pos = -1
        for i in range(len(intervals)):
            if intervals[i].start >= newInterval.start:
                pos = i
                break
        if pos == -1:
            if intervals and newInterval.start <= intervals[-1].end:
                intervals[-1].end = max(intervals[-1].end, newInterval.end)
            else:
                intervals.append(newInterval)
            return(intervals)
        
        res = intervals[:pos] 
        intervals= [newInterval] + intervals[pos:]
        
        for j in range(len(intervals)):
            
            if res and intervals[j].start <= res[-1].end:
                res[-1].end = max(intervals[j].end, res[-1].end)
            else:
                res.append(intervals[j])
        return(res)
        
  # Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        pos = -1
        for i in range(len(intervals)):
            if intervals[i].start >= newInterval.start:
                pos = i
                break
        if pos == -1:
            intervals.append(newInterval)
            res = []
        else:
            res = intervals[:pos] 
            intervals= [newInterval] + intervals[pos:]
        
        for j in range(len(intervals)):
            if res and intervals[j].start <= res[-1].end:
                res[-1].end = max(intervals[j].end, res[-1].end)
            else:
                res.append(intervals[j])
        return(res)      
