# https://leetcode.com/problems/connecting-cities-with-minimum-cost/

from typing import List
from typing import Optional
import math

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x):
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

    def getSize(self, u):
        pu = self.find(u)
        return self.size[pu]

class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        edges = [[con[2], con[0], con[1]] for con in connections]
        edges.sort()
        ans = 0
        uf = UnionFind(n+1)
        for edge in edges:
            if uf.find(edge[1]) != uf.find(edge[2]):
                uf.union(edge[1], edge[2])
                ans += edge[0]
            if uf.getSize(edge[1]) == n:
                break
        if uf.getSize(1) != n:
            return -1
        return ans

s = Solution()
sol = s.minimumCost(4, [[1,2,3],[3,4,4]])
print(sol)