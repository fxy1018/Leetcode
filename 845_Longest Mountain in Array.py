'''
Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

B.length >= 3
There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain. 

Return 0 if there is no mountain.
Example 1:

Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
Example 2:

Input: [2,2,2]
Output: 0
Explanation: There is no mountain.
 

Note:

0 <= A.length <= 10000
0 <= A[i] <= 10000

'''
class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        count = 0
        stackUp = []
        i = 0
        while i <len(A):
            if not stackUp:
                stackUp.append(A[i])
                i+=1
            elif A[i] > stackUp[-1]:
                stackUp.append(A[i])
                i+=1
            elif A[i] == stackUp[-1]:
                stackUp = [A[i]]
                i+=1
            elif A[i] < stackUp[-1]:
                length = len(stackUp)
                if length == 1:
                    stackUp.pop()
                    stackUp.append(A[i])
                    i += 1
                else:
                    pre = stackUp[-1]
                    while i<len(A) and A[i] < pre:
                        pre = A[i]
                        i += 1
                        length += 1
                    if length >=3:
                        count = max(count, length)
                    stackUp = []
                    stackUp.append(A[i-1])
        return(count)
