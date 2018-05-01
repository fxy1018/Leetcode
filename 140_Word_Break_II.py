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



# 采用深度优先遍历的策略，我们把字符串分为前后两个部分，如果前半部分在单词组中，那么我们就只要递归拆分它的后半部分。那么怎么将字符串分为前后两个部分呢，我们可以直接依次把单词组中的单词与当前字符串的头部进行比较，如果相同，则递归后半部分。
# 光采用dfs效率低下，因为会有很多重复的情况，假设字符串为abcd...，且我们的单词组中有{a,b,c,ab,bc,abc}，那么以d开头的字符串就要被拆分四次。为了避免这样的情况，可以用过哈希的方法来缓存之前已经计算出来的结果。我们通过一个字典来缓存字符串和它对应的拆分结果。
 
#time complexity: O(2^n)
 
class Solution2(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        #backtracking strategy
        dic = {}
        wordDict = set(wordDict)
        return(self.helpFun(s, dic, wordDict))
        
    def helpFun(self, s, dic, wordDict) :
        if not s:
            return([None])
        
        if s in dic:
            return(dic[s])
        res = []
        for word in wordDict:
            n = len(word)
            if s[:n] == word:
                for r in self.helpFun(s[n:], dic, wordDict): 
                    if r:
                        res.append(word+" "+ r)
                    else:
                        res.append(word)
                
        dic[s] = res
        return res
    
class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        wordSet = set(wordDict)
        memo = {}
        
        return(self.helpFun(s, wordSet, memo, 0))
        
    def helpFun(self, s, wordSet, memo, pos):
        if pos >= len(s):
            return([None])
            
        if pos in memo:
            return(memo[pos])
        res = []
        for word in wordSet:
            n = len(word)
            if s[pos: pos+n] == word:
                for r in self.helpFun(s, wordSet, memo, pos+n):
                    if r:
                        res.append(word + " " + r) 
                    else:
                        res.append(word)
                    
        memo[pos] = res
        return(res)       
            

 
 
 
                
s = Solution4()
# print(s.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
print(s.wordBreak("aaaaaaa", ["aaaa","aa","a"]))


