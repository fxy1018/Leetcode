'''
Given many words, words[i] has weight i.

Design a class WordFilter that supports one function, WordFilter.f(String prefix, String suffix). It will return the word with given prefix and suffix with maximum weight. If no word exists, return -1.

Examples:
Input:
WordFilter(["apple"])
WordFilter.f("a", "e") // returns 0
WordFilter.f("b", "") // returns -1
Note:
words has length in range [1, 15000].
For each test case, up to words.length queries WordFilter.f may be made.
words[i] has length in range [1, 10].
prefix, suffix have lengths in range [0, 10].
words[i] and prefix, suffix queries consist of lowercase letters only.


'''
#method1: regex TIME LIMIT EXCEEDED

#regexp
import re
class WordFilter(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.words = words
        self.weights = {}
        for i, word in enumerate(words):
            self.weights[word] = i
        

    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        res = -1
        for word in self.words:
            find1 = re.search("^"+prefix+'.*',word)
            find2 = re.search(".*"+suffix +"$", word)
            if find1 and find2:
                res = max(res, self.weights[word])
        return(res)

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
