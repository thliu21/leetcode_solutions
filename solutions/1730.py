from typing import List
from typing import Optional
import math
import heapq
from collections import Counter, deque

class Solution:
    def shortestPath(self, grid: List[List[str]]) -> int:
        visited = set()
        queue = deque([])
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "*":
                    queue.append((i, j, 0))
                    visited.add((i, j))
                    break
        m_x = [0, 0, 1, -1]
        m_y = [1, -1, 0, 0]
        while queue:
            head = queue.popleft()
            for i in range(4):
                nx = m_x[i] + head[0]
                ny = m_y[i] + head[1]
                if nx >= 0 and nx < n and ny >= 0 and ny < m and (nx, ny) not in visited:
                    if grid[nx][ny] == "#":
                        return head[2] + 1
                    elif grid[nx][ny] == "O":
                        queue.append((nx, ny, head[2]+1))
                        visited.add((nx, ny))
        return -1

s = Solution()
sol = s.getFood([["O","*"],["#","O"]])
print(sol)