"""
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.

"""


'''
Created on Jan 16, 2017

@author: fanxueyi
'''
#首先，要遍历无向图，需要使用Hash Map来当作visited数组，防止重复访问而造成程序中的死循环
#遍历图有两种方式 - BFS & DFS，本题均可采用
#BFS - 使用Queue (prefer)
#DFS - 递归或者使用Stack，对于DFS，每次clone一个node的时候，就要把它所有的neighbor加入到新clone的node的neighbor中，此时recursivly调用dfs，如果没有visited过 - 新建一个node，否则直接从map中找到返回
#在visited数组中，key值为原来的node，value为新clone的node，如果一个node不存在于map中，说明这个node还未被clone，将它clone后放入queue中继续处理neighbors




# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    #method1: BFS
    
    def __init__(self):
        self.visited = {}
        
    def cloneGraph(self, node):
        if not node:
            return(node)
        
        
        queue = [node]
        root = UndirectedGraphNode(node.label)
        self.visited[node] = root
        while queue:
            curr_old_node = queue.pop(0)
            for neighbor in curr_old_node.neighbors:
                if neighbor not in self.visited:
                    newNode = UndirectedGraphNode(neighbor.label)
                    self.visited[neighbor] = newNode
                    queue.append(neighbor)
                    self.visited[curr_old_node].neighbors.append(newNode)
                else:
                    self.visited[curr_old_node].neighbors.append(self.visited[neighbor])
        return(root)
            
        
        
         #method2: DFS
    
    def __init__(self):
        self.visited = {}
        
    def cloneGraph(self, node):
        if not node:
            return(node)
        return(self.dfs(node))
        
    def dfs(self, node):
        if node in self.visited:
            return(self.visited[node])
        newNode = UndirectedGraphNode(node.label)
        self.visited[node] = newNode
        for neighbor in node.neighbors:
            newNode.neighbors.append(self.dfs(neighbor))
        return(newNode)

