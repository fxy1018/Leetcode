'''
Given a balanced parentheses string S, compute the score of the string based on the following rule:

() has score 1
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.
 

Example 1:

Input: "()"
Output: 1
Example 2:

Input: "(())"
Output: 2
Example 3:

Input: "()()"
Output: 2
Example 4:

Input: "(()(()))"
Output: 6
 

Note:

S is a balanced parentheses string, containing only ( and ).
2 <= S.length <= 50

'''
class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        for c in S:
            if not stack:
                stack.append(c)
            elif c == "(":
                stack.append(c)
            else:
                tmp = 0
                while stack[-1] != "(":
                    tmp += stack.pop()
                stack.pop()
                if tmp == 0:
                    stack.append(1)
                else:
                    stack.append(tmp*2)
        tmp = 0
        while stack:
            tmp += stack.pop()
        
        return(tmp)
