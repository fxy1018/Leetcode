'''

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".


再得到一个数字后要看看之前有没有出现这个数。为了节省搜索时间，我们采用哈希表来存数每个小数位上的数字。还有一个小技巧，由于我们要算出小数每一位，采取的方法是每次把余数乘10，再除以除数，得到的商即为小数的下一位数字。等到新算出来的数字在之前出现过，则在循环开始出加左括号，结束处加右括号。
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
    
