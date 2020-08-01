def gameOfLife(self, board):
    dirs = [(-1,0),(1,0),(0,-1),(0,1),(1,1),(-1,-1),(1,-1),(-1,1)]
    for i in range(len(board)):
        for j in range(len(board[i])):
            neighbours = 0
            for x,y in dirs:
                iDiff, jDiff = i+x, j+y
                if 0 <= iDiff < len(board) and 0 <= jDiff < len(board[0]):
                    if abs(board[iDiff][jDiff]) == 1:
                        neighbours+=1
            
            if board[i][j] == 1 and neighbours < 2:
                board[i][j] = -1
            elif board[i][j] == 1 and neighbours > 3:
                board[i][j] = -1
            elif board[i][j] == 0 and neighbours == 3:
                board[i][j] = -2
                
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == -1:
                board[i][j] = 0
            elif board[i][j] == -2:
                board[i][j] = 1
    
    return board