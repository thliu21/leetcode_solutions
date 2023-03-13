from typing import List
from typing import Optional
import math
import heapq
from collections import Counter, deque

class Solution:
    def shortestPath(self, grid: List[List[str]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])
        if n == 1 and m == 1:
            return 0
        queue = deque([[0, 0, k, 0]])
        visited = [[[False for _ in range(k+1)] for _ in range(m)] for _ in range(n)]
        visited[0][0][k] = True
        m_x = [0, 0, 1, -1]
        m_y = [1, -1, 0, 0]
        while queue:
            head = queue.popleft()
            if head[0] == n-1 and head[1] == m-1:
                return head[3]
            for i in range(4):
                nx = m_x[i] + head[0]
                ny = m_y[i] + head[1]
                if nx >= 0 and nx < n and ny >= 0 and ny < m:
                    if nx == n-1 and ny == m-1:
                        return head[3] + 1
                    elif grid[nx][ny] == 0 and not visited[nx][ny][head[2]]:
                        queue.append([nx, ny, head[2], head[3]+1])
                        visited[nx][ny][head[2]] = True
                    elif grid[nx][ny] == 1 and head[2] > 0 and not visited[nx][ny][head[2]-1]:
                        queue.append([nx, ny, head[2]-1, head[3]+1])
                        visited[nx][ny][head[2]-1] = True
        return -1

s = Solution()
sol = s.shortestPath([[0,0,1,0,0,0,0,1,0,1,1,0,0,1,1],[0,0,0,1,1,0,0,1,1,0,1,0,0,0,1],[1,1,0,0,0,0,0,1,0,1,0,0,1,0,0],[1,0,1,1,1,1,0,0,1,1,0,1,0,0,1],[1,0,0,0,1,1,0,1,1,0,0,1,1,1,1],[0,0,0,1,1,1,0,1,1,0,0,1,1,1,1],[0,0,0,1,0,1,0,0,0,0,1,1,0,1,1],[1,0,0,1,1,1,1,1,1,0,0,0,1,1,0],[0,0,1,0,0,1,1,1,1,1,0,1,0,0,0],[0,0,0,1,1,0,0,1,1,1,1,1,1,0,0],[0,0,0,0,1,1,1,0,0,1,1,1,0,1,0]], 27)
print(sol)