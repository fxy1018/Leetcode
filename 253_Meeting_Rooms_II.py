"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.

"""


'''
Created on Jan 30, 2017

@author: fanxueyi
'''
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

import heap_priority_queue
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        
        # methods1: too slow
        """
        intervals = sorted(intervals, key=lambda x: x.end)
        room = 0
        while intervals:
            lastest_inter = intervals.pop()
            start = lastest_inter.start
            for i in intervals[::-1]:
                if i.end <= start:
                    intervals.remove(i)
                    start = i.start
            room += 1
                    
        return(room)
        """
        
        #use heap_priority_queue
        intervals = sorted(intervals, key=lambda x: x.start)
        room = 0
        heap=[]
        heap_priority_queue.heapify(heap)
        for i in intervals:
            if len(heap) == 0:
                heap_priority_queue.heappush(heap,i.end)
                room +=1
                continue
            if heap[0] <= i.start:
                # heap_priority_queue pop and push
                heap_priority_queue.heapreplace(heap, i.end)
            else:
                heap_priority_queue.heappush(heap, i.end)
                room +=1
        return(room)

