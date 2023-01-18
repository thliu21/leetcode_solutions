"""
水题，判有根树最远叶子
"""

from typing import List

class Node:
    def __init__(self, eid, inform_time) -> None:
        self.eid = eid
        self.children = []
        self.inform_time = inform_time

class Solution:
    def distance(self, node) -> int:
        if len(node.children) == 0:
            return 0
        longest = 0
        for child in node.children:
            longest = max(longest, self.distance(child) + node.inform_time)
        return longest

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        employees = [Node(i, time) for (i, time) in zip(range(n), informTime)]
        boss = None
        for idx, m in enumerate(manager):
            if m == -1:
                boss = idx
            else:
                employees[m].children.append(employees[idx])
        return self.distance(employees[boss])

s = Solution()
sol = s.numOfMinutes(6, 2, [2,2,-1,2,2,2], [0,0,1,0,0,0])
print(sol)