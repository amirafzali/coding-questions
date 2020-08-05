def setZeroes(self, matrix):
    if not matrix: return matrix
    rowZero = colZero = matrix[0][0] == 0
    matrix[0][0] = matrix[0][0] if matrix[0][0] != 0 else 1
    
    for i in range(len(matrix[0])):
        if matrix[0][i] == 0: rowZero = True
            
    for i in range(len(matrix)):
        if matrix[i][0] == 0: colZero = True
            
    for i in range(1,len(matrix)):
        for j in range(1,len(matrix[i])):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
                
    for i in range(len(matrix[0])):
        if matrix[0][i] == 0:
            for j in range(len(matrix)):
                matrix[j][i] = 0
        if rowZero: matrix[0][i] = 0
                
    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            for j in range(len(matrix[i])):
                matrix[i][j] = 0
        if colZero: matrix[i][0] = 0
            
    return matrix