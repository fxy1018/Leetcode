'''

We had some 2-dimensional coordinates, like "(1, 3)" or "(2, 0.5)".  Then, we removed all commas, decimal points, and spaces, and ended up with the string S.  Return a list of strings representing all possibilities for what our original coordinates could have been.

Our original representation never had extraneous zeroes, so we never started with numbers like "00", "0.0", "0.00", "1.0", "001", "00.01", or any other number that can be represented with less digits.  Also, a decimal point within a number never occurs without at least one digit occuring before it, so we never started with numbers like ".1".

The final answer list can be returned in any order.  Also note that all coordinates in the final answer have exactly one space between them (occurring after the comma.)

Example 1:
Input: "(123)"
Output: ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]
Example 2:
Input: "(00011)"
Output:  ["(0.001, 1)", "(0, 0.011)"]
Explanation: 
0.0, 00, 0001 or 00.01 are not allowed.
Example 3:
Input: "(0123)"
Output: ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"]
Example 4:
Input: "(100)"
Output: [(10, 0)]
Explanation: 
1.0 is not allowed.
 

Note:

4 <= S.length <= 12.
S[0] = "(", S[S.length - 1] = ")", and the other elements in S are digits.

O(N**3)
'''

class Solution:
    def ambiguousCoordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        #consider two level, first is ",", very easy to seperate numbre into two part
        #for each part, consider add "."
        if not S:
            return([])
        
        if len(S) < 1:
            return([S])
        
        memo = {}
        
        S = S[1:len(S)-1]
        res = []
        for i in range(1, len(S)):
            left = S[:i]
            right = S[i:]
            leftRes = self.helpFun(left, memo)
            rightRes = self.helpFun(right, memo)
            if leftRes and rightRes:
                for l in leftRes:
                    for r in rightRes:
                        res.append("(" + l + ", " + r + ")")
        return(res)
                        
    def helpFun(self, string, memo):
        if len(string) == 1:
            return([string])
        
        if string in memo:
            return(memo[string])
        
        l = len(string)
        res = []
        #consider four situation
        if string[0] == "0" and string[-1]=="0":
            res = []
        elif string[0] == "0" and string[-1]!="0":
            res = [string[0] + "." + string[1:]]
        elif string[0] != "0" and string[-1] == "0":
            res = [string]
        else:
            res.append(string)
            for i in range(1, l):
                res.append(string[:i] + "." + string[i:])
        memo[string] = res
        return(res)
