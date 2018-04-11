'''

Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.

'''

class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if not A or not B:
            return(-1)
            
        lenA = len(A)
        lenB = len(B)
        if lenB%lenA == 0:
            longA = A * ((lenB//lenA)*2)
        else:
            longA = A * ((lenB//lenA + 1)*2)
        
        for i in range(len(longA)-lenA):
            if longA[i: i+lenB] == B:
                if (i+lenB)%lenA == 0:
                    return((i+lenB)//lenA )
                else:
                    return((i+lenB)//lenA  + 1)
        return(-1)
        
