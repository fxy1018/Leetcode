class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        #check row:
        for row in board:
            numList= set()
            for item in row:
                if item != "." and item in numList:
                    return False
                else:
                    numList.add(item)
        
        #check column:
        length = len(board)
        for i in range(length):
            numList = set()
            for j in range(length):
                 if board[j][i] != "." and board[j][i] in numList:
                    return False
                 else:
                    numList.add(board[j][i])
        
        #check block:
        for i in range(0, length, 3):
            for j in range(0, length, 3):
                if not self.isBlockValid(board, i, j):
                    return False
                
        return True
    
    def isBlockValid(self, board, row, column):
        numList = set()
        for i in range(3):
            for j in range(3):
                if board[row+i][column+j] != "." and board[row+i][column+j] in numList:
                    return False
                else:
                    numList.add(board[row+i][column+j])
        return True
