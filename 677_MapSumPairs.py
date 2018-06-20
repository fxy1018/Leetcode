'''
Implement a MapSum class with insert, and sum methods.

For the method insert, you'll be given a pair of (string, integer). The string represents the key and the integer represents the value. If the key already existed, then the original key-value pair will be overridden to the new one.

For the method sum, you'll be given a string representing the prefix, and you need to return the sum of all the pairs' value whose key starts with the prefix.

Example 1:
Input: insert("apple", 3), Output: Null
Input: sum("ap"), Output: 3
Input: insert("app", 2), Output: Null
Input: sum("ap"), Output: 5


'''
class Node(object):
    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.isLeaf = False
        self.val = 0
     
    
class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node(0)
        

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        root = self.root
        for letter in key:
            if letter not in root.children:
                root.children[letter] = Node(letter)
            root = root.children[letter]
        root.isLeaf = True
        root.val = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        root = self.root
        for c in prefix:
            if c not in root.children:
                return(0)
            root = root.children[c]
        return(self.getSum(root))
    
    
    def getSum(self, root):
        if not root.children:
            return(root.val)
        res = root.val
        for c in root.children:
            res += self.getSum(root.children[c])
        return(res)
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
