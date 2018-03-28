"""

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Show Tags
Hide Similar Problems


"""
'''
Created on Feb 6, 2017

@author: fanxueyi
'''
##use BFS
"""
这个题目用到的方法是图形学中的一个常用方法：Flood fill算法，其实就是从一个点出发对周围区域进行目标颜色的填充。背后的思想就是把一个矩阵看成一个图的结构，每个点看成结点，而边则是他上下左右的相邻点，然后进行一次广度或者深度优先搜索。
 
这道题首先四个边缘上的‘O’点都不是被surrounded的，这是很直接能看出的，麻烦的是与这些边界上的‘O’点毗邻的其他‘O’点，这些点由于跟边缘上的'O'毗邻，所以也米有被‘X’包裹住。所以我们的想法是：把边界上的‘O’点都找出来，对它们做Flood Fill, 把联通的‘O’区域找出来，把这个区域的点统统由‘O’替换为其他字符比如‘$’。这样没有被替换仍旧为‘O’的那些点，就是被‘X’包裹的。这样整体扫描一次，剩下的所有'O'都应该被替换成'X'，而'$'那些最终应该是还原成'O'。
 
复杂度分析上，我们先对边缘做Flood fill算法，因为只有是'O'才会进行，而且会被替换成'#'，所以每个结点改变次数不会超过一次，因而是O(m*n)的复杂度，最后一次遍历同样是O(m*n)，所以总的时间复杂度是O(m*n)。
 
空间上没懂，看了别人的思路。空间上就是递归栈（深度优先搜索）或者是队列（广度优先搜索）的空间，同时存在的空间占用不会超过O(m+n)（以广度优先搜索为例，每次队列中的结点虽然会往四个方向拓展，但是事实上这些结点会有很多重复，假设从中点出发，可以想象最大的扩展不会超过一个菱形，也就是n/2*2+m/2*2=m+n，所以算法的空间复杂度是O(m+n)）
 
方法选择当然DFS和BFS都可以，DFS如果用递归来实现，像Flood Fill算法里那样，图形或者矩阵一般很大，递归容易导致堆栈溢出。所以即使用DFS，也要用Stack来写。
"""


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        
        nrow = len(board)
        ncol = len(board[0])
        queue = []
        #top board:
        for c in range(ncol):
            if board[0][c] == "O":
                queue.append((0,c))
                self.bfs(board, queue)
        #left board:
        for r in range(nrow):
            if board[r][0] == "O":
                queue.append((r,0))
                self.bfs(board, queue)
        #bottom board:
        for c in range(ncol):
            if board[nrow-1][c] == "O":
                queue.append((nrow-1,c))
                self.bfs(board, queue)
        #right board:
        for r in range(nrow):
            if board[r][ncol-1] == "O":
                queue.append((r,ncol-1))
                self.bfs(board, queue)
                
        #change signs
        for r in range(nrow):
            for c in range(ncol):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "1":
                    board[r][c] = "O"
    
    def bfs(self, board, queue):
        nrow = len(board)
        ncol = len(board[0])
        while queue:
            i,j = queue.pop(0)
            board[i][j] = "1"
            if i > 0:
                if board[i-1][j] == "O" and ((i-1,j) not in queue):
                    queue.append((i-1,j))
            if j > 0:
                if board[i][j-1] == "O"and ((i,j-1) not in queue):
                    queue.append((i,j-1))
            if i < nrow-1 and ((i+1,j) not in queue):
                if board[i+1][j] == "O":
                    queue.append((i+1,j))
            if j < ncol-1 and ((i,j+1) not in queue):
                if board[i][j+1] == "O":
                    queue.append((i,j+1))
 class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        #start from edge:
        if not board:
            return
        
        row = len(board)
        col = len(board[0])
        for i in range(row):
            if board[i][0] == "O":
                self._bfs(i, 0, board)
            if board[i][col-1]=="O":
                self._bfs(i, col-1, board)
        for j in range(col):
            if board[0][j] == "O":
                self._bfs(0, j, board)
            if board[row-1][j]=="O":
                self._bfs(row-1, j, board)
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "$":
                    board[i][j] = "O"
        return
    
    def _bfs(self, i, j, board):
        queue = [(i,j)]
        while queue:
            i,j = queue[0]
            board[i][j] = '$'
            queue = queue[1:]
            if i > 0:
                if board[i-1][j] == "O" and (i-1, j) not in queue:
                    queue.append((i-1,j))
            if j > 0:
                if board[i][j-1] == "O" and (i, j-1) not in queue:
                    queue.append((i,j-1))     
            if i < len(board)-1:
                if board[i+1][j] == "O" and (i+1, j) not in queue:
                    queue.append((i+1,j))
            if j < len(board[0])-1:
                if board[i][j+1] == "O" and (i, j+1) not in queue:
                    queue.append((i,j+1))
                
        
               
