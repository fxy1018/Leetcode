"""

basic method to built trie tree model

if use nested dictionaries to build it is cumbersome (space inefficient)
ex: 
'foo', 'bar', 'baz', 'barz'

{'b': {'a': {'r': {'_end_': '_end_', 'z': {'_end_': '_end_'}}, 
             'z': {'_end_': '_end_'}}}, 
 'f': {'o': {'o': {'_end_': '_end_'}}}}

I have intall PyTrie package 


Trie or Prefix tree implemention:

1. addWord
2. searchWord O(M), M is the maximum string length
3. deleteWord

"""

'''
Created on Mar 3, 2017

@author: fanxueyi
'''

class TreeNode(object):
    def __init__(self):
        self.value = ""
        self.children = dict()
        self.isLeaf = False
    
class Trie(object):
    def __init__(self):
        self.root = TreeNode()
    
    def insert(self,word):
        node = self.root
        for letter in word:
            if letter not in node.children:
                child = TreeNode()
                child.value = letter
                node.children[letter] = child
            node = node.children[letter]
        node.isLeaf = True
        
    def search(self, word):
        node = self.root
        for letter in word:
            if letter in node.children:
                node = node.children[letter]
            else:
                return(False)
        
        return(node.isLeaf)
    

        
        
        
        
        
    
