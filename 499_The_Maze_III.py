'''
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up (u), down (d), left (l) or right (r), but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction. There is also a hole in this maze. The ball will drop into the hole if it rolls on to the hole.

Given the ball position, the hole position and the maze, find out how the ball could drop into the hole by moving the shortest distance. The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the hole (included). Output the moving directions by using 'u', 'd', 'l' and 'r'. Since there could be several different shortest ways, you should output the lexicographically smallest way. If the ball cannot reach the hole, output "impossible".

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The ball and the hole coordinates are represented by row and column indexes.


'''

class Solution(object):
    def findShortestWay(self, maze, ball, hole):
        """
        :type maze: List[List[int]]
        :type ball: List[int]
        :type hole: List[int]
        :rtype: str
        """
        visited = set([])
        queue = []
        heapq.heappush(queue, (0, "", ball))
        
        dirs = {"d":(1, 0), "l":(0,-1), "r":(0, 1), "u":(-1, 0)}
        while queue:
            step, path, ball = heapq.heappop(queue)
            
            if ball[0] == hole[0] and ball[1] == hole[1]:
                return(path)
            
            if (ball[0], ball[1]) in visited:
                continue
                
            visited.add((ball[0], ball[1])) 
            for di in ["d", "u", "r", "l"]:
                dir = dirs[di]
                x = ball[0] + dir[0]
                y = ball[1] + dir[1]
                count = 0
                while x>=0 and y>=0 and x<len(maze[0]) and y<len(maze) and maze[x][y] == 0:
                    x += dir[0]
                    y += dir[1]
                    count += 1
                    
                    if x == hole[0] and y == hole[1]:
                        break
                if x == hole[0] and y == hole[1]:
                    heapq.heappush(queue, (step+count, path+di, (x, y)))
                else:
                    heapq.heappush(queue, (step+count, path+di, (x-dir[0], y-dir[1])))
                
        return("impossible")
                
            
