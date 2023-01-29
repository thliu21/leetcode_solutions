"""
https://leetcode.com/problems/cheapest-flights-within-k-stops/description/
n个点，e个有向有权边，求k步之内最短路

一开始以为是迭代加深后来发现时间上会有问题，用bfs做扩张，必须按层搜。
在入队时，必须带上当前距离，否则会出现当前层结果影响上一层的情况，可能导致答案变小。
"""

from collections import deque
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        inf = 1<<30
        k += 1
        edges = [[] for _ in range(n)]
        for flight in flights:
            edges[flight[0]].append((flight[1], flight[2]))
        costs = [1<<30 for _ in range(n)] 
        costs[src] = 0
        queue = deque([(src, 0)])
        while len(queue) > 0 and k > 0:
            m = len(queue)
            while m > 0:
                node, cost = queue.popleft()
                for edge in edges[node]:
                    if cost + edge[1] < costs[edge[0]]:
                        costs[edge[0]] = cost + edge[1]
                        queue.append((edge[0], costs[edge[0]]))
                m -= 1
            k -= 1
        if costs[dst] == inf:
            return -1
        return costs[dst]

s = Solution()
sol = s.findCheapestPrice(4, [[0,1,1],[0,2,5],[1,2,1],[2,3,1]], 0, 3, 1)
print(sol)