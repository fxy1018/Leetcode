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

