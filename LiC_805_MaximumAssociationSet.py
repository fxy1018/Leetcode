'''
Amazon sells books, every book has books which are strongly associated with it. Given ListA and ListB,indicates that ListA [i] is associated with ListB [i] which represents the book and associated books. Output the largest set associated with each other(output in any sort). You can assume that there is only one of the largest set.

 Notice
The number of books does not exceed 5000.
Example
Given ListA = ["abc","abc","abc"], ListB = ["bcd","acd","def"], return["abc","acd","bcd","dfe"].

Explanation:
abc is associated with bcd, acd, dfe, so the largest set is the set of all books
Given ListA = ["a","b","d","e","f"], ListB = ["b","c","e","g","g"], return ["d","e","f","g"].

Explanation:
The current set are [a, b, c] and [d, e, g, f], then the largest set is [d, e, g, f]

'''

class Solution:
    """
    @param ListA: The relation between ListB's books
    @param ListB: The relation between ListA's books
    @return: The answer
    """
    def maximumAssociationSet(self, ListA, ListB):
        # Write your code here
        #union find + graph
        bookMap = {}
        for i in range(len(ListA)):
            if ListA[i] in bookMap:
                bookMap[ListA[i]].append(ListB[i])
            else:
                bookMap[ListA[i]]= [ListB[i]]
            
            if ListB[i] in bookMap:
                bookMap[ListB[i]].append(ListA[i])
            else:
                bookMap[ListB[i]]= [ListA[i]]
        
        res = set([])
        visited = set([])
        for key in bookMap:
            if key not in res and key not in visited:
                tmpRes = self._bfs(bookMap, key, visited)
                if len(tmpRes) > len(res):
                    res = tmpRes
                   
        return(list(res))
    
    def _bfs(self, bookMap, key, visited):
        queue = [key]
        tmpvisited = set([])
        
        while queue:
            curr = queue[0]
            queue = queue[1:]
            tmpvisited.add(curr)
            visited.add(curr)
            queue.extend([b for b in bookMap[curr] if b not in tmpvisited])
        return(tmpvisited)
