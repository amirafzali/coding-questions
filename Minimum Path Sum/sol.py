def minPathSum(self, grid):
    for i in range(len(grid)-1,-1,-1):
        for j in range(len(grid[i])-1,-1,-1):
            if i == len(grid)-1 and j==len(grid[i])-1: continue
            smallest = float('inf')
            if j < len(grid[i])-1:
                smallest = grid[i][j+1]
            if i < len(grid)-1:
                smallest = min(smallest,grid[i+1][j])
            grid[i][j] += smallest
        
    return grid[0][0]