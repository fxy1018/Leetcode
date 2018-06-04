'''
Description
A gene string can be represented by an 8-character long string, with choices from "A", "C", "G", "T".

Suppose we need to investigate about a mutation (mutation from "start" to "end"), where ONE mutation is defined as ONE single character changed in the gene string.

For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.

Also, there is a given gene "bank", which records all the valid gene mutations. A gene must be in the bank to make it a valid gene string.

Now, given 3 things - start, end, bank, your task is to determine what is the minimum number of mutations needed to mutate from "start" to "end". If there is no such a mutation, return -1.

1.Starting point is assumed to be valid, so it might not be included in the bank.
2.If multiple mutations are needed, all mutations during in the sequence must be valid.
3.You may assume start and end string is not the same.

Have you met this question in a real interview?  
Example
Example 1:

start: "AACCGGTT"
end:   "AACCGGTA"
bank: ["AACCGGTA"]

return: 1
Example 2:

start: "AACCGGTT"
end:   "AAACGGTA"
bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

return: 2
Example 3:

start: "AAAAACCC"
end:   "AACCCCCC"
bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]

return: 3


'''

class Solution:
    """
    @param start: 
    @param end: 
    @param bank: 
    @return: the minimum number of mutations needed to mutate from "start" to "end"
    """
    def minMutation(self, start, end, bank):
        # Write your code here
        #bfs
        bank = set(bank)
        if end not in bank:
            return(-1)
            
        queue = [(start, 0)]
        visit = set([start])
        while queue:
            word, level = queue[0]
            queue = queue[1:]
            
            if word == end:
                return(level)
            
            for i in range(8):
                for c in "ATCG":
                    tmp = word[:i] + c + word[i+1:]
                    if tmp in bank and tmp not in visit:
                        queue.append((tmp, level+1))
                        visit.add(tmp)
        return(-1)
            
