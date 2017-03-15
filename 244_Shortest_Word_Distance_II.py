"""

This is a follow up of Shortest Word Distance. The only difference is now you are given the list of words and your method will be called repeatedly many times with different parameters. How would you optimize it?

Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.


"""

'''
Created on Mar 13, 2017

@author: fanxueyi
'''

class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.wordHash = {}
        for i in range(len(words)):
            if words[i] not in self.wordHash:
                self.wordHash[words[i]] = [i]
            else:
                self.wordHash[words[i]].append(i)
        

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        word1Index =  self.wordHash[word1]
        word2Index =  self.wordHash[word2]
        
        res = float("inf")
        #O(n**2)
        # for i in word1Index:
        #     for j in word2Index:
        #         res = min(res, abs(j-i))
        
        #O(n)
        i = j = 0
        m, n = len(word1Index), len(word2Index)
        
        while i < m and j < n:
            res = min(res, abs(word1Index[i]-word2Index[j]))
            if word1Index[i] < word2Index[j]:
                i += 1
            else:
                j += 1
        return(res)
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)