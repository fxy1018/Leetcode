"""

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples: 
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
For example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2



tip: use two heap to maintain the data, max_heap, min_heap

in python, heapq implement min-heap(priority queue)

here I implement max-heap

"""

'''
Created on Mar 10, 2017

@author: fanxueyi

'''

from heapq import heappush, heappop

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minHeap = []
        self.maxHeap = []
    

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if not self.minHeap and not self.maxHeap:
            self.maxHeapPush(self.maxHeap, num)
            return
        
        max_top = self.maxHeap[0]
        if num <= max_top:
            self.maxHeapPush(self.maxHeap, num)
        else:
            heappush(self.minHeap, num) 
            
        print(self.minHeap, self.maxHeap)
        
        if len(self.minHeap) == len(self.maxHeap) + 2:
            self.maxHeapPush(self.maxHeap, heappop(self.minHeap))
        
        if len(self.maxHeap) == len(self.minHeap) + 2:
            heappush(self.minHeap, self.maxHeapPop(self.maxHeap))

            
                    

    def findMedian(self):
        """
        :rtype: float
        """
        minHeapSize = len(self.minHeap)
        maxHeapSize = len(self.maxHeap)
        
        if not self.minHeap and not self.maxHeap:
            return(None)
        
        if not self.minHeap:
            min_top = 0
        else:
            min_top = self.minHeap[0] 
            
        if not self.maxHeap:
            max_top = 0
        else:
            max_top = self.maxHeap[0] 
        
        if (minHeapSize + maxHeapSize) & 1 == 0:
            return((min_top+max_top)/2.0)
        else:
            return(max_top if maxHeapSize > minHeapSize else min_top)
        
        
    
    
    def maxHeapPush(self, heap, item):
        heap.append(item)
        self.maxShiftUp(heap, len(heap)-1)
        
    def maxHeapPop(self, heap):
        heap[0], heap[-1] = heap[-1], heap[0]
        res = heap.pop()
        self.maxShiftDown(heap, 0)
        return(res)
    
    def maxShiftUp(self, heap, index):
        while index != 0:
            parent = (index-1)//2
            if heap[parent] < heap[index]:
                self.swap(heap, parent, index)
                index = parent
            else:
                break         
    
    def maxShiftDown(self, heap, index):
        left  = index * 2 + 1
        right = index * 2 + 2
        largest = index
        while left < len(heap):
            if heap[left] > heap[index]:
                largest = left
            if right < len(heap) and heap[right] > heap[largest]:
                largest = right
            if largest != index:
                self.swap(heap, largest, index)
            else:
                break
            index = largest
            left  = index * 2 + 1
            right = index * 2 + 2
        
    def swap(self, heap, index1, index2):
        temp = heap[index1]
        heap[index1] = heap[index2]
        heap[index2] = temp
        
        
import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.leftMaxHeap =[]
        self.rightMinHeap=[]

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if len(self.leftMaxHeap) == 0:
           heapq.heappush(self.leftMaxHeap, [-num, num])
        else:
            leftTop = self.leftMaxHeap[0][1]
            if num > leftTop:
                heapq.heappush(self.rightMinHeap, num)
            else:
                heapq.heappush(self.leftMaxHeap, [-num, num])

            if len(self.leftMaxHeap)-len(self.rightMinHeap) > 1:
                tmp = heapq.heappop(self.leftMaxHeap)[1]
                heapq.heappush(self.rightMinHeap, tmp)
            elif len(self.rightMinHeap) - len(self.leftMaxHeap) > 1:
                tmp = heapq.heappop(self.rightMinHeap)
                heapq.heappush(self.leftMaxHeap, [-tmp, tmp])
        

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.leftMaxHeap) == len(self.rightMinHeap):
            return((self.leftMaxHeap[0][1]+self.rightMinHeap[0])/2.0)
        else:
            if len(self.rightMinHeap) > len(self.leftMaxHeap):
                return(self.rightMinHeap[0])
            else:
                return(self.leftMaxHeap[0][1])
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()   
    
    
                
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


obj = MedianFinder()
print(obj.findMedian())
obj.addNum(-1)
print(obj.minHeap, obj.maxHeap)
print(obj.findMedian())
obj.addNum(-2)
print(obj.minHeap, obj.maxHeap)
print(obj.findMedian())
obj.addNum(-3)
print(obj.minHeap, obj.maxHeap)
print(obj.findMedian())
obj.addNum(-4)
print(obj.minHeap, obj.maxHeap)
print(obj.findMedian())
obj.addNum(-5)
print(obj.minHeap, obj.maxHeap)
print(obj.findMedian())





