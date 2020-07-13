def numIslands(self, grid: List[List[str]]) -> int:
    
    if not grid: return 0
    count = 0
    
    m, n = len(grid), len(grid[0])
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                count+=1
                self.search(grid,i,j)
                
    return count
    
def search(self, grid, i, j):
    grid[i][j] = "0"

    dirs = [(1,0),(-1,0),(0,1),(0,-1)]

    for x,y in dirs:
        diffI, diffJ = i+x, j+y

        if 0 <= diffI < len(grid) and 0 <= diffJ < len(grid[0]) and grid[diffI][diffJ] == "1":
            self.search(grid, diffI, diffJ)

# O(N*M)
# O(N*M)