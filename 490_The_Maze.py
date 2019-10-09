'''
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.
'''

#dfs 
class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        #direction: left: (-1,0), right (1, 0), up (0, -1), down(0, 1)
        nRow = len(maze)
        nCol = len(maze[0])
        visited = [ [0]*nCol for i in range(nRow)]
        return(self.dfs(maze, start, destination, visited))
    
    def dfs(self, maze, start, destination, visited):
        if visited[start[0]][start[1]]:
            return(False)
        if start[0] == destination[0] and start[1] == destination[1]:
            return(True)

        visited[start[0]][start[1]] = 1
        
        left = start[1] - 1
        right = start[1] + 1
        up = start[0] -1 
        down = start[0] + 1

        #left run
        while left >=0 and maze[start[0]][left] == 0:
            left -= 1
        if self.dfs(maze, (start[0], left+1), destination, visited):
            return(True)
        
        #right run
        while right < len(maze[0]) and maze[start[0]][right] == 0:
            right += 1
        if self.dfs(maze, (start[0], right-1), destination, visited):
            return(True)
        
        #up run
        while up >=0 and maze[up][start[1]] == 0:
            up -= 1
        if self.dfs(maze,( up+1 , start[1]), destination, visited):
            return(True)
        
        #down run
        while down < len(maze) and maze[down][start[1]] == 0:
            down += 1
        if self.dfs(maze, (down-1, start[1]), destination, visited):
            return(True)
        
        return(False)
        
