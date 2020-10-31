class Solution:
    def DFS(self, grid, visited, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0' or visited[i][j]:
            return
        visited[i][j] = True
        self.DFS(grid, visited, i + 1, j)
        self.DFS(grid, visited, i - 1, j)
        self.DFS(grid, visited, i, j + 1)
        self.DFS(grid, visited, i, j - 1)
        
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        count = 0
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and not visited[i][j]:
                    self.DFS(grid, visited, i, j)
                    count += 1
        return count