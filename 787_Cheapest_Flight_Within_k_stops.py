class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        #dfs
        self.res = float("Inf")
        graph = {}
        visited = [src]
        for e in flights:
            graph[e[0]] = graph.get(e[0], []) + [(e[1], e[2])]
            
        self.dfs(n, graph, src, dst, K, 0, visited)
        if self.res == float("Inf"):
            return(-1)
        return(self.res)
    
    def dfs(self, n, graph, src, dst, K, val, visited):
        if K < 0:
            return        
        if src not in graph:
            return
        
        for e in graph[src]:
            if e[0] not in visited:
                if e[0] == dst:
                    self.res = min(self.res, val+e[1])
                else:
                    newVisited = visited + [e[0]]
                    self.dfs(n, graph, e[0], dst, K-1, val+e[1], newVisited)
            
            
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        #bfs
        f = collections.defaultdict(dict)
        for a, b, p in flights:
            f[a][b] = p
        
        heap = [(0, src, K+1)]
        while heap:
            p, i , k  = heapq.heappop(heap)
            if i == dst:
                return(p)
            if k > 0:
                for j in f[i]:
                    heapq.heappush(heap, (p+f[i][j], j, k-1))
        return(-1)
