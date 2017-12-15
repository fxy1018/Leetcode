###
Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.

###

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node('')
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for letter in word:
            if letter not in node.children:
                child = Node(letter)
                node.children[letter] = child
            node = node.children[letter]
        node.isLeaf = True
            
            

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        
        node = self.root
        for letter in word:
            if letter in node.children:
                node = node.children[letter]
            else:
                return(False)
        return(node.isLeaf)
        
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for letter in prefix:
            if letter not in node.children:
                return(False)
            node = node.children[letter]
        return(True)
        
        
        
class Node(object):
    def __init__(self, letter):
        self.val = letter
        self.children = {}
        self.isLeaf = False

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
