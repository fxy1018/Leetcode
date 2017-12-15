###
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
###

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node('')

    def addWord(self, word):
        """
        Adds a word into the data structure.
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
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        node = self.root
        return(self.helpFun(word, node))
  
    def helpFun(self, word, node):
        out = False
        for i in range(len(word)):
            letter = word[i]
            if letter != ".":
                if letter not in node.children:
                    return(False)
                else:
                    node = node.children[letter]
            elif letter == ".":
                new_word = word[(i+1):]
                nodes = node.children
                for key in nodes:
                    sub_node = nodes[key] 
                    out = out or self.helpFun(new_word, sub_node)
                return(out)
            elif not letter:
                return(node.isLeaf)
       
        
        
        
class Node(object):
    def __init__(self, letter):
        self.val = letter
        self.children = {}
        self.isLeaf = False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
