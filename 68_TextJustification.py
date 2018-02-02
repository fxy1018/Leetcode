'''
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Note: Each word is guaranteed not to exceed L in length.

click to show corner cases.

Corner Cases:
A line other than the last line might contain only one word. What should you do in this case?
In this case, that line should be left-justified.

比较麻烦的字符串细节实现题。需要解决以下几个问题：

1. 首先要能判断多少个word组成一行：
这里统计读入的所有words的总长curLen，并需要计算空格的长度。假如已经读入words[0:i]。当curLen + i <=L 且加curLen + 1 + word[i+1].size() > L时，一行结束。

2. 知道一行的所有n个words，以及总长curLen之后要决定空格分配：
平均空格数：k = (L - curLen) / (n-1)
前m组每组有空格数k+1：m = (L - curLen) % (n-1)

例子：L = 21，curLen = 14，n = 4
k = (21 - 14) / (4-1) = 2
m = (21 - 14) % (4-1)  = 1
A---B--C--D

3. 特殊情况：
(a) 最后一行：当读入到第i = words.size()-1 个word时为最后一行。该行k = 1，m = 0
(b) 一行只有一个word：此时n-1 = 0，计算(L - curLen)/(n-1)会出错。该行k = L-curLen, m = 0
(c) 当word[i].size() == L时。

'''


class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if maxWidth == 0 or not words:
            return([""])
        currLen  = 0 
        wordsInLine = []
        res = []
        for i in range(len(words)):
            word = words[i]
            wordLen = len(word)
            if currLen + len(wordsInLine)-1 < maxWidth:
                if currLen + wordLen + len(wordsInLine) > maxWidth:
                    #end last line
                    line = self.createLine(wordsInLine, currLen, maxWidth)
                    res.append(wordsInLine)
                    currLen = wordLen
                    wordsInLine = [word]
                elif currLen + wordLen + len(wordsInLine) == maxWidth:
                    #end line
                    line = self.createLine(wordsInLine+[word], currLen, maxWidth)
                    res.append(wordsInLine)
                    currLen = 0
                    wordsInLine = []
                else:
                    wordsInLine.append(word)
                    currLen += wordLen
    
        return(res)
    
    def createLine(self, words, currLen, maxWidth):
        spaces = maxWidth-currLen
        if len(words)==1:
            return(words[0])
        
        elif spaces == 0:
            return(" ".join(words))
    
        else:
            sep_num, remain = divmod(spaces, len(words)-1)
            sep = ""*sep_num
            res = sep.join(words)
            res += "" * remain
            return(res)
            
            
            


