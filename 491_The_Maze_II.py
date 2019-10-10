'''
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, find the shortest distance for the ball to stop at the destination. The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included). If the ball cannot stop at the destination, return -1.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.

 

'''
class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        visited = [[float("Inf")] * len(maze[0]) for i in range(len(maze))]
        self.dfs(maze, start, destination, visited)
        res = visited[destination[0]][destination[1]]
        if res < float("Inf"):
            return(res)
        else:
            return(-1)

    def dfs(self, maze, start, destination, visited):
    
        lStep = rStep = uStep = dStep = 0
        
        l = start[1] - 1
        r = start[1] + 1
        u = start[0] - 1
        d = start[0] + 1
        
        while l >= 0 and maze[start[0]][l] == 0:
            l -= 1
            lStep += 1
        if visited[start[0]][start[1]] + lStep < visited[start[0]][l+1]:
            visited[start[0]][l+1] = visited[start[0]][start[1]] + lStep
            self.dfs(maze, (start[0], l+1), destination, visited)
            
        
        while r < len(maze[0]) and maze[start[0]][r] == 0:
            r += 1
            rStep += 1
        if visited[start[0]][start[1]] + rStep < visited[start[0]][r-1]:
            visited[start[0]][r-1] = visited[start[0]][start[1]] + rStep
            self.dfs(maze, (start[0], r-1), destination, visited)
        
        while u >= 0 and maze[u][start[1]] == 0:
            u -= 1
            uStep += 1
        if visited[start[0]][start[1]] + uStep < visited[u+1][start[1]]:
            visited[u+1][start[1]] = visited[start[0]][start[1]] + uStep
            self.dfs(maze, (u+1, start[1]), destination, visited)
            
        
        while d < len(maze) and maze[d][start[1]] == 0:
            d += 1
            dStep += 1
        if visited[start[0]][start[1]] + dStep < visited[d-1][start[1]]:
            visited[d-1][start[1]] = visited[start[0]][start[1]] + dStep 
            self.dfs(maze, (d-1, start[1]), destination, visited)
            
        
      
      
class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        visited = [[float("Inf")] * len(maze[0]) for i in range(len(maze))]
        visited[start[0]][start[1]] = 0
        self.dfs(maze, start, visited)
        res = visited[destination[0]][destination[1]]
        if res < float("Inf"):
            return(res)
        else:
            return(-1)

    def dfs(self, maze, start, visited):
    
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for d in dirs:
            x = start[0] + d[0]
            y = start[1] + d[1]
            count = 0
            while (x>=0 and y>=0 and x <len(maze) and y<len(maze[0]) and maze[x][y]==0):
                x += d[0]
                y += d[1]
                count += 1
            if visited[start[0]][start[1]] + count < visited[x-d[0]][y-d[1]]:
                visited[x-d[0]][y-d[1]] = visited[start[0]][start[1]] + count
                self.dfs(maze, (x-d[0], y-d[1]), visited)
        
            
        
        
        
        
        
            
            
   #bfs
   class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        visited = [[float("Inf")] * len(maze[0]) for i in range(len(maze))]
        visited[start[0]][start[1]] = 0
        queue = [start]
        
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while queue:
            start = queue.pop(0)
            for d in dirs:
                x = start[0] + d[0]
                y = start[1] + d[1]
                count = 0
                while (x>=0 and y>=0 and x <len(maze) and y<len(maze[0]) and maze[x][y]==0):
                    x += d[0]
                    y += d[1]
                    count += 1
                if visited[start[0]][start[1]] + count < visited[x-d[0]][y-d[1]]:
                    visited[x-d[0]][y-d[1]] = visited[start[0]][start[1]] + count
                    queue.append((x-d[0], y-d[1]))
        
        
        
        res = visited[destination[0]][destination[1]]
        if res < float("Inf"):
            return(res)
        else:
            return(-1)

    
        
#bfs + priority queue (Dijkstra Algorithm)
class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        visited = [[0] * len(maze[0]) for i in range(len(maze))]
        queue = []
        heapq.heappush(queue, (0, start))
        
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while queue:
            dis, start = heapq.heappop(queue)
            if start[0] == destination[0] and start[1] == destination[1]:
                return(dis)
            visited[start[0]][start[1]] = 1
            for d in dirs:
                x = start[0] + d[0]
                y = start[1] + d[1]
                count = 0
                while (x>=0 and y>=0 and x <len(maze) and y<len(maze[0]) and maze[x][y]==0):
                    x += d[0]
                    y += d[1]
                    count += 1
                if visited[x-d[0]][y-d[1]] == 0:
                    heapq.heappush(queue, (dis+count, (x-d[0], y-d[1])))
        
        return(-1)

    
        
        
        
        
            
            
            
        
