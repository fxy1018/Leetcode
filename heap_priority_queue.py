"""
in python, heapq module implement heap queue, which is priority queue

heapq.heappush(heap, item) : Push the value item onto the heap, maintaining the heap invariant.
heapq.heappop(heap) : Pop and return the smallest item from the heap, maintaining the heap invariant. 
heapq.heappushpop(heap,item) : Push item on the heap, then pop and return the smallest item from the heap. 
heapq.heapify(x) : Transform list x into a heap, in-place, in linear time.
heapq.heapreplace(heap,item) : Pop and return the smallest item from the heap, and also push the new item. The heap size doesn’t change. 

implement heap and priority queue with array

for heap: 
    method: heapify, getTop, insert (push), pop, swap


"""


'''
Created on Mar 6, 2017

@author: fanxueyi
'''
