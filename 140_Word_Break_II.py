"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. You may assume the dictionary does not contain duplicate words.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].



"""
'''
Created on Mar 1, 2017

@author: fanxueyi
'''

#Time Limit Exceeded
class Solution1(object):
    def __init__(self):
        self.result = []
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        #backtracking strategy
        elements = []
        wordDict = set(wordDict)
        self.helpFun(s, elements, wordDict)
        return(self.result)
    
    def helpFun(self, s, elements, wordDict) :
        n = len(s)
        for i in range(n+1):
            if s[:i] in wordDict:
                newElements = elements+[s[:i]]
                newS = s[i:]
                self.helpFun(newS, newElements, wordDict)
        if not s:
            return
        if s in wordDict:
            elements.append(s)
            self.result.append(" ".join(elements))
            return

#Using DFS directly will lead to TLE, here I used HashMap to save the previous results to prune duplicated branches
class Solution (object):
    def __init__(self):
        self.result = []
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        #backtracking strategy
        created = {}
        wordDict = set(wordDict)
        self.helpFun(s, wordDict, created)
        return(self.result)
    
    def helpFun(self, s, wordDict, created) :
        if not s:
            return([None])
        
        if s in created:
            self.result.append(created[s])
            return(created[s])
        res = []
        for word in wordDict:
            n = len(word)
            if s[:n] == word:
                elements = self.helpFun(s[n:], wordDict, created)
                for e in elements:
                    if e:
                        res.append(word + " " + e)
                    else:
                        res.append(word) 
            created[s] = res
            return res 
        return(self.helpFun(s,wordDict, created))
                
s = Solution()
# print(s.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
print(s.wordBreak("aaaaaaa", ["aaaa","aa","a"]))


