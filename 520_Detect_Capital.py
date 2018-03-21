'''
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital if it has more than one letter, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
Example 1:
Input: "USA"
Output: True
Example 2:
Input: "FlaG"
Output: False

'''
#method1: regexp
import re
class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        allCap = "^[A-Z]+$"
        allSmall = "^[a-z]+$"
        firstCap = "^[A-Z][a-z]+$"
        
        if re.search(allCap, word):
            return(True)
        if re.search(allSmall, word):
            return(True)
        if re.search(firstCap, word):
            return(True)
        return(False)

class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
        #method2:
        cap = 0
        small = 0

        for c in word:
            if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                cap += 1
            else:
                small += 1
        return((word[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and cap == 1) or small == len(word) or cap == len(word))
