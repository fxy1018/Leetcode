'''

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".

'''

class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        signN = 1 if numerator >= 0 else -1
        signD = 1 if denominator >= 0 else -1
        
        div,mod = divmod(abs(numerator),abs(denominator))
        res = str(div)
        if signN * signD == -1 and numerator != 0:
            res = "-" + res
        if mod == 0: 
            return(res)
        res += '.'
        dec = ""
        visited = {mod:0}
        pos = 0
        while mod != 0:
            div, mod = divmod(mod*10, abs(denominator))
            dec  += str(div)
            
            if mod in visited:
                tmpPos = visited[mod]
                return(res+dec[:tmpPos] + "(" + dec[tmpPos:] + ")")
            else:
                pos += 1
                visited[mod] = pos 
                
        return(res+dec)
    
