def uniquePaths(self, m, n):
    ways = [[0 for i in range(m)] for i in range(n)]
    
    ways[0][0] = 1
    
    for i in range(n):
        for j in range(m):
            if i > 0: ways[i][j] += ways[i-1][j]
            if j > 0: ways[i][j] += ways[i][j-1]
                
    return ways[-1][-1]