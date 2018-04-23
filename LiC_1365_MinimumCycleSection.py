'''
Given an array of int, find the length of the minimum cycle section.

 Notice
The length of array do not exceed 100000。
Each element is in the int range 。

Example
Given array = [1,2,1,2,1,2], return 2.

Explanation:
The minimum cycle section is [1,2]，and the length is 2.
Given array = [1,2,1,2,1], return 2.

Explanation:
The minimum cycle section is [1,2]，and the length is 2, although the last 2 is not given, we still consider the cycle section is [1,2].
Given array = [1,2,1,2,1,4], return 6.

Explanation:
The minimum cycle section is [1,2,1,2,1,4], and the length is 6.
'''

#brute-force
class Solution:
    """
    @param array: an integer array
    @return: the length of the minimum cycle section
    """
    def minimumCycleSection(self, array):
        # Write your code here
        if not array:
            return(0)
        i = 0
        while i < len(array):
            l = len(array[0:i+1])
            isCycle = True
            for z in range(l):
                c = array[z]
                isCycle, index = self.helpFun(z,l,c,array)
                if not isCycle:
                    i = index
                    break
            if isCycle:
                return(l)
        return(len(array))
        
    def helpFun(self, z, l ,c, array):
        for j in range(z, len(array), l):
            if array[j] != c:
                if array[j] == array[0]:
                    return(False, j-1)
                return([False, j])
        return(True,z)
                
            
