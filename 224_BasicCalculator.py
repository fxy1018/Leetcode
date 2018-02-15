'''
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

You may assume that the given expression is always valid.

Some examples:
"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23
Note: Do not use the eval built-in library function.

'''

class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        
        if not s:
            return(None)
        
        s2 = s
        out = 0
        while s2:
            if s2[0] == " ":
                s2 = s2[1:]
            elif s2[0] != ")" :
                if s2[0] in "+-(":
                    stack.append(s2[0])
                    s2 = s2[1:]
                else:
                    num  = ""
                    while s2 and s2[0] in "12345567890":
                        num += s2[0]
                        s2 = s2[1:]
                    stack.append(num)     
            else:
                stack2 = []
                while stack and stack[-1] != "(":
                    stack2.append(stack.pop())
                stack.pop()
                stack.append(self.getResult(stack2))
                s2 = s2[1:] 
                
        return(self.getResult(stack[::-1]))
    
    def getResult(self, stack):
        out = 0
        operator = 1

        while stack:
            char = stack.pop()
            if char == "-":
                operator = -1
            elif char == "+":
                operator = 1
            else:
                out += operator*int(char)
                operator = 1
        return(out)

    #modify logic
class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        out = 0
        sign = 1
        num = 0
        for i in range(len(s)):
            char = s[i]
            if char in "12345567890":
                num = 10*num + int(char)
            elif char == "+":
                out += sign * num
                sign = 1
                num = 0
            elif char == "-":
                out += sign * num
                sign = -1
                num = 0
            elif char == "(":
                stack.append(out)
                stack.append(sign)
                sign = 1
                out = 0
                
            elif char == ")":
                out += sign * num
                num = 0
                out *= stack.pop()
                out += stack.pop()
        
        out+= sign*num
        return(out)
