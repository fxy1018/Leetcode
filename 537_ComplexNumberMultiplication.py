'''
Given two strings representing two complex numbers.

You need to return a string representing their multiplication. Note i2 = -1 according to the definition.

Example 1:
Input: "1+1i", "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
Example 2:
Input: "1+-1i", "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
Note:

The input strings will not have extra blank.
The input strings will be given in the form of a+bi, where the integer a and b will both belong to the range of [-100, 100]. And the output should be also in this form.

'''

class Solution:
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        x, y = self._getNums(a)
        m, n = self._getNums(b)
        p1 = x*m
        p2 = y*m + x*n
        p3 = y*n
        
        p13 = p1-p3
        if p13 == 0:
            return('0+'+str(p2)+"i")
        else:
            return(str(p13) + "+" + str(p2) + 'i')
    
    def _getNums(self, s):
        a, c = s.split("+")
        b = c[0:len(c)-1]
        return(int(a), int(b))
