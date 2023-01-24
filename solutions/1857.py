"""
拓扑排序DP
"""

from typing import List
from typing import Optional

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        size = len(colors)
        color_ids = [ord(c)-ord('a') for c in colors]
        inds = [0 for _ in range(size)]
        out_edges = [[] for _ in range(size)]
        max_chars = [[0 for _ in range(26)] for _ in range(size)]
        for edge in edges:
            out_edges[edge[0]].append(edge[1])
            inds[edge[1]] += 1
        for idx, color_id in enumerate(color_ids):
            max_chars[idx][color_id] += 1
        
        queue = [idx for idx, ind in enumerate(inds) if ind == 0]
        in_q = [ind == 0 for idx, ind in enumerate(inds)]
        visited = [False for _ in range(size)]
        count = len(visited)
        
        ans = 1
        while len(queue) > 0:
            head = queue.pop(0)
            visited[head] = True
            in_q[head] == False
            for edge in out_edges[head]:
                if visited[edge]:
                    return -1 # loop found
                inds[edge] -= 1
                if inds[edge] == 0:
                    queue.append(edge)
                    in_q[edge] = True
                for char in range(26):
                    temp = 1 if char == color_ids[edge] else 0
                    temp += max_chars[head][char]
                    max_chars[edge][char] = max(
                        max_chars[edge][char],
                        temp
                    )
                    ans = max(ans, max_chars[edge][char])

        for v in visited:
            if not v:
                return -1

        return ans

s = Solution()
sol = s.largestPathValue("hhqhuqhqff", [[0,1],[0,2],[2,3],[3,4],[3,5],[5,6],[2,7],[6,7],[7,8],[3,8],[5,8],[8,9],[3,9],[6,9]])
print(sol)