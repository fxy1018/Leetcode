"""

This is a follow up of Shortest Word Distance. The only difference is now word1 could be the same as word2.

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

word1 and word2 may be the same and they represent two individual words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “makes”, word2 = “coding”, return 1.
Given word1 = "makes", word2 = "makes", return 3.

Note:
You may assume word1 and word2 are both in the list.


"""


'''


Created on Mar 13, 2017

@author: fanxueyi
'''
class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
    
        # dis = len(words) + 1
        # if word1 == word2:
        #     pre = -float("inf")
            
        #     for i in range(len(words)):
        #         if words[i] == word1:
        #             dis = min(dis, abs(i - pre))
        #             pre = i
                
        # else:
        #     index1 = -1
        #     index2 = -1
            
        #     for i in range(len(words)):
        #         if words[i] == word1:
        #             index1 = i
        #         if words[i] == word2:
        #             index2 = i
        #         if index1 != -1 and index2 != -1:
        #             dis = min(dis, abs(index1 - index2))
        # return(dis)
        
        
        #modified
        n = len(words)
        p1 = p2 = -n
        dis = n
        for i in range(n):
            if words[i] == word1:
                p1 = i
                dis = min(dis, abs(i-p2))
                if word1 == word2:
                    p2 = p1
            elif word1 != word2 and words[i] == word2:
                p2 = i
                dis = min(dis, abs(i-p1))
                
        return(dis)
        
    
        
        
            