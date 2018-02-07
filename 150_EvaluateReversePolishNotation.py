'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

'''

class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if not tokens:
            return(None)
        if tokens[0] in ['+', '-', '*', '/']:
            return(None)
        stack = []
        for value in tokens:
            if value not in {'+', '-', '*', '/'}:
                stack.append(value)
            else:
                v1 = int(stack.pop())
                v2 = int(stack.pop())
                if value == "+":
                    stack.append(v1+v2)
                elif value == "-":
                    stack.append(v2-v1)
                elif value == "*":
                    stack.append(v1*v2)
                elif value == "/":
                    stack.append(v2/v1)
        return(int(stack[-1]))
