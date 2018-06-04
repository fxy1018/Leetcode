'''

Description
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

The expression string contains only non-negative integers, +, -, *, / operators , open ( and closing parentheses ) and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-2147483648, 2147483647]

Do not use the eval built-in library function.

Have you met this question in a real interview?  
Example
"1 + 1" = 2
" 6-4 / 2 " = 4
"2*(5+5*2)/3+(6/2+8)" = 21
"(2+6* 3+5- (3*14/7+2)*5)+3"=-12

'''

class Solution:
    """
    @param s: the expression string
    @return: the answer
    """
    def calculate(self, s):
        # Write your code here
        stack = []
        i = 0
        sign = 1
        while i < len(s):
            if s[i] == "(":
                start = i
                count = 1
                i += 1
                while i < len(s) and count != 0:
                    if s[i] == "(":
                        count += 1
                    elif s[i] ==")":
                        count -= 1
                    i += 1
                tmp = self.calculate(s[start+1:i-1])
                stack.append(sign*tmp)
            elif s[i] == " ":
                i+=1 
            elif s[i] in "0123456789":
                number = 0
                while i < len(s) and s[i] in "0123456789":
                    number = 10* number  + int(s[i])
                    i+=1
                stack.append(sign * number)
                sign = 1
                number = 0 
            elif s[i] in  "+":
                sign = 1
                i += 1
            elif s[i] in  "-":
                sign = -1
                i += 1
                
            elif s[i] in "*/":
                multiSign = s[i]
                top = stack.pop()
                i+= 1
                number = 0
                while i < len(s) and s[i]==" ":
                    i+=1
                if s[i] == "(":
                    start = i
                    count = 1
                    i+=1
                    while i < len(s) and count != 0:
                        if s[i] == "(":
                            count += 1
                        elif s[i] ==")":
                            count -= 1
                        i += 1
                    number = self.calculate(s[start+1:i-1])
                else:
                    while i < len(s) and s[i] in "0123456789":
                        number = 10*number + int(s[i])
                        i+=1
                        
                if multiSign == "*":
                    stack.append(top*number)
                if multiSign == "/":
                    if top * number < 0 :
                        stack.append(math.ceil(top/number))
                    else:
                        stack.append(top // number)
                number = 0
        
        return(sum(stack))
