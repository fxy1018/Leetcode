'''
There is an undirected graph consisting of n nodes numbered from 0 to n - 1. You are given a 0-indexed integer array vals of length n where vals[i] denotes the value of the ith node.

You are also given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.

A star graph is a subgraph of the given graph having a center node containing 0 or more neighbors. In other words, it is a subset of edges of the given graph such that there exists a common node for all edges.

The image below shows star graphs with 3 and 4 neighbors respectively, centered at the blue node.


The star sum is the sum of the values of all the nodes present in the star graph.

Given an integer k, return the maximum star sum of a star graph containing at most k edges.

'''

class Solution(object):
    def maxStarSum(self, vals, edges, k):
        """
        :type vals: List[int]
        :type edges: List[List[int]]
        :type k: int
        :rtype: int
        """
        nodeHash = {}
        for i in range(len(vals)):
            nodeHash[i] = []
        
        for node1, node2 in edges:
            if vals[node1] > 0:
                nodeHash[node2].append(vals[node1])
            if vals[node2] > 0:
                nodeHash[node1].append(vals[node2])
        
        maxStarSum = -100000
        for node, neighbors in nodeHash.items():
            maxStarSum = max(maxStarSum, self.getMaxSum(node, neighbors, vals, k))
        return maxStarSum
    
    def getMaxSum(self, node, neighbors, vals, k):
        neighborsValue = sum(sorted(neighbors, reverse= True)[:k])
        return vals[node] + neighborsValue

        
