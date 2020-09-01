class Solution(object):
    def candyCrush(self, board):
        changed = True
        while changed:
            changed = False
            for i in range(len(board)):
                for j in range(len(board[0])):
                    self.mark(board,i,j)
            if self.drop(board): changed = True
                        
        return board

    def mark(self, board, i, j):        
        if i < len(board)-2 and abs(board[i][j]) == abs(board[i+1][j]) == abs(board[i+2][j]):
            board[i][j] = board[i+1][j] = board[i+2][j] = -abs(board[i][j])
        
        if j < len(board[0])-2 and abs(board[i][j]) == abs(board[i][j+1]) == abs(board[i][j+2]):
            board[i][j] = board[i][j+1] = board[i][j+2] = -abs(board[i][j]) 
            
    
    def drop(self, board):
        moved = False
        for j in range(len(board[0])):
            pos = len(board)-1
            for i in range(len(board)-1,-1,-1):
                if board[i][j] > 0:
                    board[i][j], board[pos][j] = board[pos][j], board[i][j]
                    pos-=1
                elif board[i][j] < 0:
                    board[i][j] = 0
                    moved = True
        
        return moved