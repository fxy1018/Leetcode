'''

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: 2, [[1,0]] 
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
             course 0. So the correct course order is [0,1] .
Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.


'''
#time limit exceed
class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        if not prerequisites:
            return([x for x in range(numCourses)])
        #bfs to get topological sort results with adjacency matrices
        res = []
        edges = [[0] * numCourses for _ in range(numCourses)]
        
        for pre in prerequisites:
            edges[pre[1]][pre[0]] = 1
       
        noIncomingNodes = []
        for i in range(numCourses):
            hasOne = 0
            for j in range(numCourses):
                if edges[j][i] == 1: 
                    hasOne = 1
            if hasOne ==0:
                noIncomingNodes.append(i)
       
        while noIncomingNodes:
            node = noIncomingNodes[0]
            noIncomingNodes = noIncomingNodes[1:]
            res.append(node)
            for i in range(numCourses):
                if edges[node][i] == 1:
                    edges[node][i] = 0
                    if len([edges[j][i] for j in range(numCourses) if edges[j][i] == 1]) == 0:
                        noIncomingNodes.append(i)
                    
        for i in range(numCourses):
            for j in range(numCourses):
                if edges[j][i] == 1: 
                    return([])
        return(res)
 
 class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # write your code here
        if not prerequisites:
            return([x for x in range(numCourses)])
        #bfs to get topological sort results with adjacency matrices
        res = []
        nodeIncomingHash = {}
        nodeOutcomingHash = {}
        for i in range(numCourses):
            nodeIncomingHash[i] = []
            nodeOutcomingHash[i] = []
        for r in prerequisites:
            nodeIncomingHash[r[0]] = nodeIncomingHash.get(r[0], []) + [r[1]]
            nodeOutcomingHash[r[1]] = nodeOutcomingHash.get(r[1], []) + [r[0]]
         
        queue = [key for key in nodeIncomingHash if len(nodeIncomingHash[key])==0]
    
        while queue:
            node = queue[0]
            queue = queue[1:]
            res.append(node)
            nextNodes = nodeOutcomingHash[node]
            
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
                return([])
        return(res)
 
