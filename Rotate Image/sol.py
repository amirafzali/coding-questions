def rotate(self, matrix):
    for i in range(len(matrix)):
        for j in range(i,len(matrix)):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
            
    for i in range(len(matrix)): matrix[i] = matrix[i][::-1]