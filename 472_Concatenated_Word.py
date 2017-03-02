"""
Given a list of words (without duplicates), please write a program that returns all concatenated words in the given list of words.

A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Example:
Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
 "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
Note:
The number of elements of the given array will not exceed 10,000
The length sum of elements in the given array will not exceed 600,000.
All the input string will only include lower case letters.
The returned elements order does not matter.

"""


'''
Created on Mar 1, 2017

@author: fanxueyi
'''



class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        words = set(words)
        out = []
        for word in words:
            words.remove(word)
            if self.isConcatenatedWord(word,words):
                out.append(word)
            words.add(word)
        return(out)
    
    def isConcatenatedWord(self,word,words):
        if word in words:
            return(True)
            
        for i in range(1,len(word)):
            if word[:i] in words and self.isConcatenatedWord(word[i:], words):
                return(True)
            
        return(False)
        