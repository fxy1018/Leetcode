'''

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5
Note: Do not use the eval built-in library function.

'''

#use regular expression
import re
class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = re.sub(" ", "", s)
        i = 0
        stack = []
        pre = 0
        sign = ""
        while i < len(s):
            c = s[i]
            
            if c in "+-":
                stack.append(c)
                i+=1
            elif c in "*/":
                num, newI = self.getNum(s, i+1)
                i = newI
                preNum = stack.pop()
                if c =="*":
                    stack.append(preNum * num)
                else:
                    stack.append(preNum // num)
                
            else:
                num, newI = self.getNum(s, i)
                stack.append(num)
                i = newI
        res = stack[0]
        j = 1
        while j < len(stack) : 
            if stack[j] == "+":
                res += stack[j+1]
                
            if stack[j] == "-":
                res -= stack[j+1]
            j = j + 2
        return(res)
                
        
        
    def getNum(self, s, i):
        pre = 0
        
        while i <len(s) and s[i] in "0123456789" :
            pre = 10*pre + ord(s[i])-ord("0")
            i+=1
        return(pre, i)
        
class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
       
        pre = 0
        stack = []
        sign = "+"
        for i in range(len(s)):
            if s[i] in "0123456789":
                pre = 10*pre + ord(s[i]) - ord("0")
            if s[i] in "+-*/" or i == len(s)-1:
                if sign == "+":
                    stack.append(pre)
                if sign == "-":
                    stack.append(-1 * pre)
                if sign == "*":
                    preNum = stack.pop()
                    stack.append(preNum * pre)
                if sign == "/":
                    preNum = stack.pop()
                    if preNum * pre < 0 :
                        stack.append(math.ceil(preNum/pre))
                    else:
                        stack.append(preNum // pre)
                sign = s[i]
                pre = 0
        return(sum(stack))
        
        
