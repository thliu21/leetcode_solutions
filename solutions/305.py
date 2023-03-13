from typing import List
from typing import Optional
import math
import heapq
from collections import Counter, deque

class UnionFind:
    def __init__(self, n):
        self.parent = [-1 for _ in range(n)]
        self.size = [0] * n

    def find(self, x):
        if x == -1:
            return -1               
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv: return False
        if self.size[pu] > self.size[pv]:  # Union by larger size
            self.size[pu] += self.size[pv]
            self.parent[pv] = pu
        else:
            self.size[pv] += self.size[pu]
            self.parent[pu] = pv
        return True

    def setLand(self, x):
        self.parent[x] = x
        self.size[x] = 1

    def isLand(self, x):
        return self.parent[x] >= 0

class Solution:
    def numIslands2(self, n: int, m: int, positions: List[List[int]]) -> List[int]:
        def rank(i, j):
            return m*i + j
        uf = UnionFind(n*m)
        mx = [0, 1, 0, -1]
        my = [1, 0, -1, 0]
        islands = 0
        ans = []
        for pos in positions:
            cur_rank = rank(pos[0], pos[1])
            if not uf.isLand(cur_rank):
                islands += 1
                uf.setLand(cur_rank)
                for i in range(4):
                    nx = pos[0] + mx[i]
                    ny = pos[1] + my[i]
                    if nx < 0 or ny < 0 or nx >= n or ny >= m:
                        continue
                    new_rank = rank(nx, ny)
                    if uf.isLand(new_rank) and uf.union(cur_rank, new_rank):
                        islands -= 1
            ans.append(islands)
        return ans

s = Solution()
sol = s.numIslands2(3, 3, [[0,0],[0,1],[1,2],[2,1]])
print(sol)