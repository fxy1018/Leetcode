'''

Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
 

Note:

S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.

'''

class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        res = [len(S)] * len(S)
        
        locC = []
        for i, letter in enumerate(S):
            if letter == C:
                locC.append(i)
                res[i] = 0
        
        for pos in locC:
            for i, letter in enumerate(S):
                if letter != C:
                    res[i] = min(res[i], abs(pos-i))
        return(res)
    
    
 class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        pre = -float("Inf")
        
        ans = []
        
        for i, letter in enumerate(S):
            if letter == C:
                pre = i
            ans.append(i - pre)
        
        pre = float('Inf')
        
        for i in range(len(S)-1, -1, -1):
            if S[i] == C:
                pre = i
            ans[i] = min(ans[i], pre-i)
        
        return(ans)
