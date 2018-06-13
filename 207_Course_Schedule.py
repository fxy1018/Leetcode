"""
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.

click to show more hints.

Hints:
This problem is equivalent to finding if a cycle exists in a directed graph. If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera explaining the basic concepts of Topological Sort.
Topological sort could also be done via BFS.

"""

'''
Created on Jan 25, 2017

@author: fanxueyi
'''

"""
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.

click to show more hints.

Hints:
This problem is equivalent to finding if a cycle exists in a directed graph. If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera explaining the basic concepts of Topological Sort.
Topological sort could also be done via BFS.

"""

'''
Created on Jan 25, 2017

@author: fanxueyi
'''

class Solution(object):
    def __init__(self):
        self.visited =[]
        self.has_cycle=False
        self.tempv =[]
        self.courses={}
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        #method1: topological sort via DFS
        self.courses = {}
        for edge in  prerequisites:
            if edge[0] not in self.courses:
                self.courses[edge[0]] = [edge[1]]
            else:
                self.courses[edge[0]].append(edge[1])
          
        print(self.courses)     
        for i in range(numCourses):
            if i not in self.courses:
                self.courses[i]=[]
        
        for v in self.courses.keys():
            if v not in self.visited:
                self.dfs(prerequisites, v)
        return(not self.has_cycle)
                
    def dfs(self, prerequisites, vertex):
        if vertex in self.tempv:
            self.has_cycle =True
            return
        vs = self.courses.get(vertex)
        
        if vertex not in self.visited:
            self.tempv.append(vertex)  
            for v in vs:
                self.dfs(prerequisites, v)
            self.visited.append(vertex)
            self.tempv.remove(vertex)


            
s=Solution()
print(s.canFinish(3, [[2,0],[2,1]]))

class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        #Kahn's algorithm: topological sort based on BFS
        if not prerequisites:
            return(True)
        
        #create two hash, one is node -> next node, one is next node -> node
        comingEdgeHash = {}
        toEdgeHash = {}
        
        for i in range(numCourses):
            comingEdgeHash[i] = []
            toEdgeHash[i] = []

        for p in prerequisites:
            toEdgeHash[p[0]].append(p[1])
            comingEdgeHash[p[1]].append(p[0])
     
        visit = []
        noIncomingNode = set([])
        
        
        for n in comingEdgeHash:
            if not comingEdgeHash[n]:
                noIncomingNode.add(n)
        
        
        while noIncomingNode:
            node = noIncomingNode.pop()
            visit.append(node)
            print(node)
            nextNodes = [n for n in toEdgeHash[node]]
            for m in nextNodes:
                prerequisites.remove([node, m])
                toEdgeHash[node].remove(m)
                comingEdgeHash[m].remove(node)
                if not comingEdgeHash[m]:
                    noIncomingNode.add(m)
                   
        if prerequisites:
            return(False)
        else:
            return(True)
class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        #dfs + recur
        if not prerequisites:
            return(True)
        
        #create two hash, one is node -> next node, one is next node -> node
        toEdgeHash = {}
        
        for i in range(numCourses):
            toEdgeHash[i] = []

        for p in prerequisites:
            toEdgeHash[p[0]].append(p[1])
            
        visit = [0] * numCourses
        
        for i in range(numCourses):
            if not self._dfs(i, toEdgeHash, visit):
                return(False)
    
        return(True)
        
    def _dfs(self, i, toEdgeHash, visit):
        if visit[i] == -1:
            return(False)
        if visit[i] == 1:
            return(True)
        visit[i] = -1
        for j in toEdgeHash[i]:
            if not self._dfs(j, toEdgeHash, visit):
                return(False)
        visit[i] = 1
        return(True)
 '''
 if node v has not been visited, then mark it as 0.
if node v is being visited, then mark it as -1. If we find a vertex marked as -1 in DFS, then their is a ring.
if node v has been visited, then mark it as 1. If a vertex was marked as 1, then no ring contains v or its successors.
 
 '''
class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        #this is a question: detect a directed graph whether it has a cycle
        if not prerequisites:
            return(True)
        #create nodeHash and get all incoming edge for each node
        nodeIncomingHash = {}
        nodeOutcomingHash = {}
        for r in prerequisites:
            nodeIncomingHash[r[0]] = nodeIncomingHash.get(r[0], []) + [r[1]]
            if r[1] not in nodeIncomingHash:
                nodeIncomingHash[r[1]] = []
                
            nodeOutcomingHash[r[1]] = nodeOutcomingHash.get(r[1], []) + [r[0]]
            if r[0] not in nodeOutcomingHash:
                nodeOutcomingHash[r[0]] = []
        #put all node with no incoming edge
        queue = [key for key in nodeIncomingHash if len(nodeIncomingHash[key])==0]
        while queue:
            node = queue[0]
            queue = queue[1:]
            nextNodes = nodeOutcomingHash[node] #list reference pay attention!!!!!
            for i in range(len(nextNodes)):
                n = nextNodes[i]
                #remove the edge
                nodeIncomingHash[n].remove(node)
                if len(nodeIncomingHash[n]) == 0:
                    queue.append(n)
                else:
                    continue
        for key in nodeIncomingHash:
            if len(nodeIncomingHash[key])>0:
                return(False)
        return(True)

