'''
Given the length k, find all substrings of length k in the string str.The characters of a substring can not be repeated and output the number of substrings that satisfy such conditions (the same substring is counted only 1 times).

 Notice
|str| <= 100000.
k <= 100000.
All characters are lowercase.
Have you met this question in a real interview? 
Example
Given str = "abc", k = 2, output 2.

Explanation:
Characters are not repeated, and substrings of length k have "ab", "bc".
Given str = "abc", k = 2, output 2.

Explanation:
Characters are not repeated, and substrings of length k have "a", "b".”c”.

'''

class Solution:
    """
    @param str: The string
    @param k: The length of the substring
    @return: The answer
    """
    def findSubstring(self, str, k):
        # Write your code here
        # pointer, sliding window
        start = point = 0
        visited = []
        count = 0
        res = set([])
        while point < len(str):
            while count < k and point < len(str):
                if str[point] not in visited:
                    visited.append(str[point])
                    count += 1
                else: 
                    for i in range(len(visited)):
                        if str[point] == visited[i]:
                            start = start + i + 1
                            count = count - i
                            visited  = visited[i+1:] + [str[point]]
                            break
                point += 1
                
            if count == k:
                if str[start: start+k] not in res:
                    res.add(str[start: start+k])
                count -= 1
                start +=1
                visited = visited[1:]
        return(len(res))
                
