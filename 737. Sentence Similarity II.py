'''
Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs, determine if two sentences are similar.

For example, words1 = ["great", "acting", "skills"] and words2 = ["fine", "drama", "talent"] are similar, if the similar word pairs are pairs = [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]].

Note that the similarity relation is transitive. For example, if "great" and "good" are similar, and "fine" and "good" are similar, then "great" and "fine" are similar.

Similarity is also symmetric. For example, "great" and "fine" being similar is the same as "fine" and "great" being similar.

Also, a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"], pairs = [] are similar, even though there are no specified similar word pairs.

Finally, sentences can only be similar if they have the same number of words. So a sentence like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"].

Note:

The length of words1 and words2 will not exceed 1000.
The length of pairs will not exceed 2000.
The length of each pairs[i] will be 2.
The length of each words[i] and pairs[i][j] will be in the range [1, 20].

'''

class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        #regard pairs as a graph, word are nodes, for each word1, word2 in words1, words2 at ith position, check whether this is a path between these two words
        #use dict to represent graph
        if len(words1) != len(words2):
            return(False)
        pairsDict = {}
        for pair in pairs:
            pairsDict[pair[0]] = pairsDict.get(pair[0],[]) + [pair[1]]
            pairsDict[pair[1]] = pairsDict.get(pair[1],[]) + [pair[0]]
        #check every word pair
        for i in range(len(words1)):
            if not self.isSimilar(words1[i], words2[i], pairsDict):
                return(False)
        return(True)
      
    def isSimilar(self, word1, word2, pairsDict):
        if word1 == word2:
            return(True)
        if word1 not in pairsDict or word2 not in pairsDict:
            return(False)
        stack = [word1]
        visited = set([])
        while stack:
            curr = stack.pop()
            visited.add(curr)
            for tmpWord in pairsDict[curr]:
                if tmpWord not in visited and tmpWord not in stack:
                    if tmpWord == word2:
                        return(True)
                    stack.append(tmpWord)
        return(False)



