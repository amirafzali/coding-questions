# O(n) O(1)
class TicTacToe(object):
    def __init__(self, n):
        self.board = [[0 for j in range(n)] for i in range(n)]
        self.size = n
        

    def move(self, row, col, player):
        self.board[row][col] = player
        checkRow = checkCol = True
        checkMain = checkAlt = False
        
        for i in range(1,self.size):
            if self.board[i][col] != self.board[i-1][col]:
                checkCol = False
        
        for j in range(1,self.size):
            if self.board[row][j] != self.board[row][j-1]:
                checkRow = False
                
        if row == col:
            checkMain = True
            for i in range(1,self.size):
                if self.board[i][i] != self.board[i-1][i-1]:
                    checkMain = False
                    
        if row+col == self.size-1:
            checkAlt = True
            for i in range(1,self.size):
                if self.board[self.size-i-1][i] != self.board[self.size-i][i-1]:
                    checkAlt = False
        
        print(checkRow,checkCol,checkMain,checkAlt)
        if checkRow or checkCol or checkMain or checkAlt:
            return player
        return 0