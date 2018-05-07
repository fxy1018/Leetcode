'''
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 2^31 - 1.

Have you met this question in a real interview? 
Example
123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

'''

class Solution:
    """
    @param num: a non-negative integer
    @return: english words representation
    """
    def numberToWords(self, num):
        # Write your code here
        numHash = {0:'Zero', 1: 'One', 2: 'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six',
            7:'Seven', 8: 'Eight', 9:'Nine', 10: "Ten", 11:'Eleven', 12: "Twelve",
            13: 'Thirteen', 14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 17:'Seventeen',
            18:'Eighteen', 19:'Nineteen', 20:'Twenty', 30:'Thirty', 40:'Forty',
            50:'Fifty', 60:'Sixty', 70:'Seventy', 80:'Eighty', 90:'Ninety', 100:'Hundred',
            1000:'Thousand', 1000000:"Million", 1000000000:"Billion"
        }
        if num < 10:
            return(numHash[num])
            
        numArray = []
        while num > 0:
            mod = num % 10
            numArray = [mod] + numArray
            num = (num-mod)//10
        return(self.helpFun(numArray, numHash))
    
    def helpFun(self, num, numHash):
        l = len(num)
        if not num:
            return("")
        if l == 1:
            return(numHash[num[0]])
        if l == 2:
            d1 = num[0] * 10
            d2 = num[1]
            if d1 == 0 and d2 != 0:
                return(numHash[d2])
            if d1 == 0 and d2 == 0:
                return("")
            if d1+d2 < 20:
                return(numHash[d1+d2])
            if d2 == 0:
                return(numHash[d1])
            tmp = numHash[d1] + " " + numHash[d2]
            return(tmp)
            
        if l == 3:
            d1 = num[0]
            str2 = self.helpFun(num[1:], numHash)
            if d1 == 0: 
                if str2 == "":
                    return("")
                else:
                    return(str2)
            else:
                if str2:
                    return(numHash[d1] + " " + numHash[100] + " " + str2) 
                else:
                    return(numHash[d1] + " " + numHash[100])
                
        
        extra = l % 3
        if extra == 0:
            part1 = num[:3]
            part2 = num[3:]
        else:
            part1 = num[:extra]
            part2 = num[extra:]
            
        str1 = self.helpFun(part1,numHash) 
        str2 = self.helpFun(part2,numHash)
        
        if str1 and str2 == "":
            return(str1 + " " + numHash[10**len(part2)])
    
        elif str1 == "":
            return(str2)
        else:
            return(str1 + " " + numHash[10**len(part2)] + " " + str2)  
