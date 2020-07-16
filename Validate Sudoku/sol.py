def isValidSudoku(self, board):
    for i in range(9):
        met = set()
        for j in range(9):
            if board[i][j] in met: return False
            if board[i][j] != ".": met.add(board[i][j])
                
    for i in range(9):
        met = set()
        for j in range(9):
            if board[j][i] in met: return False
            if board[j][i] != ".": met.add(board[j][i])
    
    for i in range(9):
        met  = set()
        for j in range(3*(i//3), 3*(i//3)+3):
            for k in range(3*(i%3), 3*(i%3)+3):
                if board[j][k] in met: return False
                if board[j][k] != ".": met.add(board[j][k])
                    
    return True