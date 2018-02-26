"""

Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note: 
You may assume k is always valid, 1 <= k <= number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

"""


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #method1: use python build-in function
        num_set = set(nums)
        
        count_dict = {}
        for num in num_set:
            count_dict[num] = nums.count(num)
        
        res = sorted(count_dict.keys(), key=lambda x: count_dict.get(x), reverse=True)
        return(res[0:k])
    

class Node(object):
    def __init__(self):
        self.number = None
        self.count = 0


class Solution2(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #method2: hash + min_heap
        if not nums:
            return(nums)
        #map1 maitain the number frequency
        map1 = dict()
        for n in nums:
            map1[n] = map1.get(n, 0) + 1 
        
        #initialize the heap
        heap = [Node() for i in range(k)]
        
        #build the heap
        index = 0
        for num in map1:
            count = map1[num]
            node = Node()
            node.number = num
            node.count = count
            if index != k:
                heap[index] = node
                self.heap_insert(heap, index)
                index += 1
            else:
                if heap[0].count < node.count:
                    heap[0] = node
                    self.heap_heapify(heap, 0, k)
                
        res = []
        for i in range(0, k):
            res.append(heap[i].number)
    
        return(res)
        
        
    def heap_insert(self, heap_arr, index):
        while index!=0:
            parent = (index-1)//2
            if heap_arr[index].count < heap_arr[parent].count:
                self.swap(heap_arr, parent, index)
                index = parent
            else:
                break
     
      
        
        
    def heap_heapify(self, heap_arr, index, heapSize):
        left = (index*2)+1
        right = (index*2)+2
        smallest = index
        while left < heapSize:
            if heap_arr[left].count < heap_arr[index].count:
                smallest = left
            if right < heapSize and heap_arr[right].count < heap_arr[smallest].count:
                smallest = right
            if smallest != index : 
                self.swap(heap_arr, smallest, index)
            else:
                break;
            index = smallest
            left = (index*2)+1
            right = (index*2)+2


    def swap(self, heap_arr, index1, index2):
        temp = heap_arr[index1]
        heap_arr[index1] = heap_arr[index2]
        heap_arr[index2] = temp
        
    import heapq
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        numMap = {}
        for n in nums:
            numMap[n] = numMap.get(n,0)+1
        heap = []
        keys = list(numMap.keys())
        
        for i in range(k):
            heapq.heappush(heap, (numMap[keys[i]], keys[i]))
        
        for i in range(k,len(keys)):
            topValue, topKey = heap[0]
            if numMap[keys[i]] > topValue:
                heapq.heappop(heap)
                heapq.heappush(heap, (numMap[keys[i]], keys[i]))
        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])
            
        return(res)
        
        
        
        

    
    
    
        
        
        
s = Solution()
arr = [1,1,1,2,2,3] 
print(s.topKFrequent(arr, 2))
