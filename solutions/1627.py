"""
数学题，1-n编号的点，(p, q)两点之间有边当且仅当GCP(p,q)>Threshold。边都是无向边
n个查询求两点是否连通

并查集，事先对(t+1, n)之间的所有数字乘倍数合并，然后判集合。
"""

from typing import List
from typing import Optional

class UnionFind:
    def __init__(self, n) -> None:
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
    
    def find(self, item):
        if item != self.parent[item]:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb:
            return
        if self.size[pa] < self.size[pb]:
            pa, pb = pb, pa
        self.size[pa] += self.size[pb]
        self.parent[pb] = pa

class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        uf = UnionFind(n+1)
        for num in range(threshold+1, n+1, 1):
            for x in range(num*2, n+1, num):
                uf.union(num, x)
        ans = []
        for (p, q) in queries:
            ans.append(uf.find(p) == uf.find(q))
        return ans

s = Solution()
sol = s.areConnected(6, 1, [[1,4],[2,5],[3,6]])
print(sol)