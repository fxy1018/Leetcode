'''

Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

'''
import heapq
class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        strHash = {}
        chars = set(s)
        for c in chars:
            strHash[c] = s.count(c)
        # for c in s:
        #     strHash[c] = strHash.get(c, 0) + 1
            
        #use maxHeap
        heap = []
        for c in chars:
            heapq.heappush(heap, [-strHash[c], c])
        
        res = ""
        while heap:
            count, letter = heapq.heappop(heap)
            res += letter * (-1 * count)
        return(res)

