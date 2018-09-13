'''

'''

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        #regard equations as graph, dfs to find path between two nodes if nodes exist
        edgeWeight = self.getEdgeWeight(equations, values)
        graph = self.getGraph(equations)
        res = []
        print(edgeWeight)
        for query in queries:
            res.append(self.getPathValue(query, graph, edgeWeight))
        return(res)

    def getEdgeWeight(self, equations, values):
        res = {}        
        for i, equal in enumerate(equations):
            key = (equal[0], equal[1])
            key_r = (equal[1], equal[0])
            value = values[i]
            res[key] = value
            res[key_r] = 1/value
        return(res)

    def getGraph(self, equations):
        graph = {}
        for equal in equations:
            graph[equal[0]] = graph.get(equal[0], []) + [equal[1]]
            graph[equal[1]] = graph.get(equal[1], []) + [equal[0]]
        return(graph)

    def getPathValue(self, query, graph, edgeWeight):
        if query[0] == query[1] and query[0] in graph:
            return(1.0)
        stack = [(query[0],1)]
        visited = set()
        while stack:
            curr,currvalue = stack.pop()
            visited.add(curr)
            if curr in graph:
                for node in graph[curr]:
                    if node == query[1]:
                        return(edgeWeight[(curr, node)]*currvalue)
                    if node not in visited and node not in stack:
                        newvalue = currvalue *edgeWeight[(curr,node)]
                        stack.append((node, newvalue))
                        
        return(-1.0)   
