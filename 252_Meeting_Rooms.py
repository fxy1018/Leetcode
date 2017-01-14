"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return false.

"""



'''
Created on Jan 14, 2017

@author: fanxueyi
'''
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        if not intervals or len(intervals)==1:
            return(True)
      
        
        sorted_in = sorted(intervals, cmp = lambda x,y: cmp(x.start, y.start))
        
        for i in range(1, len(sorted_in)):
            if sorted_in[i-1].end > sorted_in[i].start:
                return False
        return(True)
        
    def canAttendMeetings2(self, intervals):
        intervals.sort(key=lambda i: i.start)
        return all(i.end <= j.start for i, j in zip(intervals, intervals[1:]))
    
    def canAttendMeetings3(self, intervals):
        intervals.sort(key=lambda i: i.start)
        return all(intervals[i-1].end <= intervals[i].start for i in range(1, len(intervals)))