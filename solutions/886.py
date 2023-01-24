"""
https://leetcode.com/problems/possible-bipartition/description/

裸题，二分图判定
"""

class Solution:
    def dfs(self, node, edges, colors, cur_color):
        if colors[node] is not None:
            if colors[node] != cur_color:
                return False
            else:
                return True
        colors[node] = cur_color
        for edge in edges[node]:
            ret = self.dfs(edge, edges, colors, not cur_color)
            if not ret:
                return False
        return True

    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        colors = [None for _ in range(n)]
        edges = [[] for _ in range(n)]
        for d in dislikes:
            edges[d[0]-1].append(d[1]-1)
            edges[d[1]-1].append(d[0]-1)
        for i in range(n):
            if colors[i] is None:
                ret = self.dfs(i, edges, colors, True)
                if not ret:
                    return False
        return True