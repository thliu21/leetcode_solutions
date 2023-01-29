"""
简单floodfill
"""

class Solution:
    def flood(self, grid, visited, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return
        if grid[i][j] == "0" or visited[i][j]:
            return
        visited[i][j] = True
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for move in moves:
            self.flood(grid, visited, i+move[0], j+move[1])

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and not visited[i][j]:
                    self.flood(grid, visited, i, j)
                    count += 1
        return count
