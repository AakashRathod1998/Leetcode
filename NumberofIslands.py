class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows, cols = len(grid), len(grid[0])
        n = 0

        def dfs(r, c):
            grid[r][c] = "2"

            for i,j in [(1,0),(-1,0),(0,1),(0,-1)]:
                ii, jj = r+i, c+j
                if 0 <= ii < rows and 0 <= jj < cols and grid[ii][jj] == '1':
                    dfs(ii, jj)
        
        for i in range(0,rows):
            for j in range(0,cols):
                if grid[i][j] == '1':
                    dfs(i,j)
                    n += 1
        
        print(n)
        return n

class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    num_islands += 1

        return num_islands

    def dfs(self, grid, r, c):
        if (
            r < 0
            or c < 0
            or r >= len(grid)
            or c >= len(grid[0])
            or grid[r][c] != "1"
        ):
            return
        grid[r][c] = "0"

        self.dfs(grid, r - 1, c)
        self.dfs(grid, r + 1, c)
        self.dfs(grid, r, c - 1)
        self.dfs(grid, r, c + 1)
