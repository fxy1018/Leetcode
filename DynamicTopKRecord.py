"""

design a data structure, print top k strng at the current time

method: two hash and one k-size min-heap

bug: can't update nodeIndexMap in time. 

data arrangement problem

"""


'''
Created on Mar 10, 2017

@author: fanxueyi
'''
import pdb

class Node(object):
    def __init__(self):
        self.string = None
        self.times = 0

class Solution(object):
    def __init__(self):
        self.heap = None
        self.strNodeMap = {}
        self.nodeIndexMap = {}
        self.index = 0
    def getTopKRecord(self, k):
        self.heap = Heap(k, self.nodeIndexMap)
    
    def addString(self, string):
        self.strNodeMap[string] = self.strNodeMap.get(string, 0) + 1
        self.nodeIndexMap[string] = self.nodeIndexMap.get(string, -1)
        currNode = Node()
        currNode.string = string
        currNode.times = self.strNodeMap[string]
        preIndex = self.nodeIndexMap[string]
        if  preIndex == -1:
            rootNode = self.heap.get(0)
            if self.index == self.heap.heapSize:
                if rootNode.times < currNode.times : 
                    self.nodeIndexMap[rootNode] = -1
                    self.heap.insert(currNode, 0)
                    self.nodeIndexMap[currNode] = 0
                    self.heap.heapify(0)
            else:
                self.nodeIndexMap[currNode] = self.index
                self.heap.insert(currNode, self.index)
                self.index += 1   
        else:
            self.heap.updateNode(currNode, preIndex)
            self.heap.heapify(preIndex)
           
    
    def printTopK(self):
        for i in range(self.heap.heapSize):
            node = self.heap.get(i)
            if not node:
                break
            print(node.string, node.times)
        

class Heap(object):
    def __init__(self, heapSize, nodeIndexMap):
        self.heap = [Node() for i in range(heapSize)]
        self.heapSize = heapSize
        self.nodeIndexMap = nodeIndexMap

    def updateNode(self, node, index):
        self.heap[index] = node

    def get(self,index):
        return(self.heap[index])
    
    def insert(self, node, index):
        self.heap[index] = node
        while index != 0:
            parent = (index-1) // 2
            if self.heap[parent].times > self.heap[index].times:
                self.__swap(parent, index)
                index = parent
            else:
                break
            
    def __swap(self, index1, index2):
        self.nodeIndexMap[self.heap[index1]] = index2
        self.nodeIndexMap[self.heap[index2]] = index1
        temp = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = temp
        
        
        
    def heapify(self, index):
        
        left  = index*2 + 1
        right = index*2 + 2
        smallest = index
        while left < self.heapSize:
            if self.heap[left].times < self.heap[index].times:
                smallest = left
            if right < self.heapSize and self.heap[right].times < self.heap[smallest].times:
                smallest = right
            if smallest != index:
                self.__swap( smallest, index)
                index = smallest
            else:
                break
            left  = index*2 + 1
            right = index*2 + 2
    
    
if __name__ == '__main__':
    record= Solution()
    record.getTopKRecord(2)
    record.addString("zuo")
    record.printTopK()
    record.addString("cheng")
    record.addString("cheng")
    record.printTopK()
    record.addString("Yun")
    record.addString("Yun")
    record.printTopK()
                
                
                
        
        
        
        