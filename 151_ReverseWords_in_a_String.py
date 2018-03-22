'''

Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Update (2015-02-12):
For C programmers: Try to solve it in-place in O(1) space.

click to show clarification.

Clarification:
What constitutes a word?
A sequence of non-space characters constitutes a word.
Could the input string contain leading or trailing spaces?
Yes. However, your reversed string should not contain leading or trailing spaces.
How about multiple spaces between two words?
Reduce them to a single space in the reversed string.

'''


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        sList = []
        word = ""
        for i in range(len(s)):
            if s[i] != " ":
                word = word + s[i]
            else:
                if word != "":
                    sList.append(word)
                word = ""
        if word != "":
            sList.append(word)
        sList = sList[::-1]
        return(" ".join(sList))
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        sList = ''
        word = ""
        for i in range(len(s)-1, -1, -1):
            if s[i] != " ":
                word = s[i] +  word  
            else:
                if word != "":
                    if sList != "":
                        sList = sList + ' ' +  word 
                    else: 
                        sList = word
                word = ""
          
        if word != "" :
            if sList == "":
                sList = word
            else:
                sList = sList + ' ' + word 
       
        return(sList)
 class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        sList = s.split(" ")
        sList2 = []
        for i in sList:
            if i != "":
                sList2.append(i)
        return(" ".join(sList2[::-1]))       
