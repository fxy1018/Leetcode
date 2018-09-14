'''
'''

class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        count = 0
        for d in data:
            if count == 0: #first byte
                if bin(d>>5) == "0b110":
                    count = 1 
                elif bin(d>>4) == "0b1110":
                    count = 2
                elif bin(d>>3) == "0b11110":
                    count = 3 
                elif bin(d>>7) != "0b0":
                    return(False)
            else:
                if bin(d>>6) != "0b10":
                    return(False)
                count -=1 
        return(count == 0)
        
