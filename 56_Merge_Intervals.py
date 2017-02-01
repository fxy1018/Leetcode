'''
Created on Jan 30, 2017

@author: fanxueyi
'''

# Definition for an interval.
class Interval(object):
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return([])
        
        intervals = sorted(intervals, key = lambda i : i.start)
        curr_inter = intervals[0]
        res = []
        for i in range(len(intervals)):
            next_inter = intervals[i]
            if curr_inter.end >= next_inter.start:
                curr_inter.end = max(curr_inter.end, next_inter.end)
            else:
                res.append(curr_inter)
                curr_inter = next_inter
        
        res.append(curr_inter)
        return(res)  
                
        
        
        
        
        
s= Solution()
i = [Interval(s=2,e=5),Interval(s=1,e=4)]

out = s.merge(i)

for i in out:
    print([i.start,i.end])
