'''

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

'''

class Node(object):
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.pre = None
        self.next = None
#strategy: hash and double linklist
class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.hash = {}  #key is the input key and value is value and node address
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.hash:
            return(-1)
        else:
            currNode = self.hash[key]
            self._remove(currNode)
            self._add(currNode)
            return(currNode.val)

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.hash:
            self._remove(self.hash[key])
        
        newNode = Node(key,value)
        self._add(newNode)
        self.hash[key] = newNode
        if len(self.hash) > self.capacity:
            removeNode = self.head.next
            self._remove(removeNode)
            del self.hash[removeNode.key]
               
    def _remove(self, node):
        pre = node.pre
        next = node.next
        pre.next = next
        next.pre = pre
        
        
    
    def _add(self, newNode):
        pre = self.tail.pre
        pre.next = newNode
        newNode.pre = pre
        newNode.next = self.tail
        self.tail.pre = newNode
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
