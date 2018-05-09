'''
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
Note:

S will be a string with length at most 12.
S will consist only of letters or digits.

'''

class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = []
        self.helpFun(0, S, "", res)
        return(res)
    
    def helpFun(self, pos, S, curr, res):
        if pos == len(S):
            res.append(curr)
            return
        if S[pos] in "1234567890":
            newCurr = curr + S[pos]
            self.helpFun(pos+1, S, newCurr, res)
        else:
            newCurr= curr + S[pos].lower()
            self.helpFun(pos+1, S, newCurr, res)
            newCurr= curr + S[pos].upper()
            self.helpFun(pos+1, S, newCurr, res)
