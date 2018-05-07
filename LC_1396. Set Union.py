'''
There is a list composed by sets. If two sets have the same elements, merge them. In the end, there are several sets left.

 Notice
The number of sets n <=1000.
The number of elements for each set m <= 100.
The element must be a non negative integer and not greater than 100000.
Have you met this question in a real interview? 
Example
Given list = [[1,2,3],[3,9,7],[4,5,10]], return 2.

Explanation:
There are 2 sets of [1,2,3,9,7] and [4,5,10] left.
Given list = [[1],[1,2,3],[4],[8,7,4,5]], return 2.

Explanation:
There are 2 sets of [1,2,3] and [4,5,7,8] left.
'''
class Solution:
    """
    @param sets: Initial set list
    @return: The final number of sets
    """
    def setUnion(self, sets):
        # Write your code here
    
        #create graph and similar to find number of island
        sets = sorted([sorted(list(set(s))) for s in sets])
        graph = {}
        for s in sets:
            self.getGraph(s, graph)
            
        res = 0
        queue = [sets[0][0]]
        while graph:
            visited = set([])
            queue = [[*graph][0]]
            queueSet= set(queue)
            while queue:
                node = queue[0]
                queue = queue[1:]
                visited.add(node)
                for n in graph[node]:
                    if n not in queueSet and n not in visited:
                        queue.append(n)
                        queueSet.add(n)
                del(graph[node])
            res += 1
        return(res)
        
        
    def getGraph(self, s, graph):
        sSet = set(s)
        for n in sSet:
            if n not in graph:
                graph[n] = set(s)
            else:
                graph[n] = set(list(graph[n]) + s)
