'''
Please judge whether there is a cycle in the directed graph with n vertices and m edges. The parameter is two int arrays. There is a directed edge from start[i] to end[i].

 Notice
2 <= n <= 10^5
1 <= m <= 4*10^5
1 <= start[i], end[i] <= n
Have you met this question in a real interview? 
Example
Given start = [1],end = [2], return "False"。

Explanation:
There is only one edge 1->2, and do not form a cycle.
Given start = [1,2,3],end = [2,3,1], return "True".

Explanation:
There is a cycle 1->2->3->1.

'''
#dfs+iteration

class Solution:
    """
    @param start: The start points set
    @param end: The end points set
    @return: Return if the graph is cyclic
    """
    def isCyclicGraph(self, start, end):
        # Write your code here
        
        #find no coming node
        keys = set(start)
        values = set(end)
        noComingNodes = []
        for key in keys:
            if key not in values:
                noComingNodes.append(key)
        
        if not noComingNodes:
            return(True)
        
        nodeHash = {}
        for i in range(len(start)):
            if start[i] in nodeHash:
                nodeHash[start[i]].append(end[i])
            else:
                nodeHash[start[i]] = [end[i]]
        allVisited = set([])
        while noComingNodes:
            visited = set([])
            stack = [ noComingNodes.pop()]
            
            while stack:
                n1 = stack.pop()
                if n1 in visited:
                    return(True)
                else:
                    allVisited.add(n1)
                    visited.add(n1)
                if n1 in nodeHash:
                    stack.extend(nodeHash[n1])
        if len(allVisited) < len(set(start+end)):
            return(True)
        return(False)
            
                
                
