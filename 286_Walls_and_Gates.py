"""

You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

For example, given the 2D grid:
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4

"""


'''
Created on Feb 6, 2017

@author: fanxueyi
'''


class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return
        
        nrow = len(rooms)
        ncol = len(rooms[0])
        
        queue = [] 
        for c in range(ncol):
            for r in range(nrow):
                if rooms[r][c] == 0:
                    queue.append([(r,c),0])
                    self.bfs(rooms, queue)
        
        return(rooms)
    def bfs(self, rooms, queue):
        nrow = len(rooms)
        ncol = len(rooms[0])
        visited = []
        while queue:
            [pos, depth] = queue.pop(0)
            i,j = pos
            
            
            """ 
            #using this strategy is TEL
            visited.append((i,j))
            rooms[i][j] = min(rooms[i][j], depth)
            
            if i > 0:
                #print(i-1, j)
                if rooms[i-1][j] != -1 and rooms[i-1][j] != 0 and ((i-1,j) not in visited) and ((i-1,j) not in [q[0] for q in queue]):
                    queue.append([(i-1,j),depth+1])   
            if j > 0:
                #print(i, j-1)
                if rooms[i][j-1] != -1 and rooms[i][j-1] != 0 and ((i,j-1) not in visited) and ((i,j-1) not in [q[0] for q in queue]):
                    queue.append([(i,j-1), depth+1])
            if i < nrow-1:
                #print(i+1, j)
                if rooms[i+1][j] != -1 and rooms[i+1][j] != 0 and ((i+1,j) not in visited) and ((i+1,j) not in [q[0] for q in queue]):
                    queue.append([(i+1,j), depth+1])
            if j < ncol-1:
                #print(i, j+1)
                if rooms[i][j+1] != -1 and rooms[i][j+1] != 0 and ((i,j+1) not in visited) and ((i,j+1) not in [q[0] for q in queue]):
                    queue.append([(i,j+1), depth+1])
            """

            if i > 0:
                if rooms[i-1][j] > depth+1:
                    rooms[i-1][j] = depth+1
                    queue.append([(i-1,j),depth+1])   
            if j > 0:
                if rooms[i][j-1] > depth+1:
                    rooms[i][j-1] = depth+1
                    queue.append([(i,j-1), depth+1])
            if i < nrow-1:
                if rooms[i+1][j] > depth+1:
                    rooms[i+1][j] = depth+1
                    queue.append([(i+1,j), depth+1])
            if j < ncol-1:
                if rooms[i][j+1] > depth+1:
                    rooms[i][j+1] = depth+1
                    queue.append([(i,j+1), depth+1])
            
        
        
        
        
        
s = Solution()
print(s.wallsAndGates([[0,2147483647,2147483647,0,-1,-1,0,0,0,-1,-1,0,2147483647,2147483647],[2147483647,-1,2147483647,-1,2147483647,0,-1,2147483647,-1,2147483647,2147483647,-1,-1,2147483647],[0,0,-1,2147483647,-1,2147483647,-1,-1,2147483647,0,0,2147483647,0,2147483647],[-1,0,2147483647,-1,0,0,-1,2147483647,0,2147483647,0,-1,0,-1]]))
                     
