"""
n个元素，每个元素可以属于m组中的一个或独立，排序要求
1. 符合前后顺序beforeItems
2. 每组元素必须相邻

每个独立元素单独为一组，先以大组建图，得到拓扑序，按照拓扑序对每个小组求拓扑序，排列起来即为答案。
任何一次拓扑排序失败则无解
"""


from typing import List

class Graph:
    def __init__(self):
        self.edges = {}
        self.ind = {}
        self.nodes = set()
    
    def add_edge(self, n, m):
        self.nodes.add(n)
        self.nodes.add(m)
        if m not in self.ind:
            self.ind[m] = 0
        if n not in self.edges:
            self.edges[n] = []
        if m not in self.edges[n]:
            self.edges[n].append(m)
            self.ind[m] += 1

    def add_node(self, n):
        self.nodes.add(n)

    def topo_sort(self) -> List[int]:
        ret = []
        zero_ind = []
        ind_copy = self.ind.copy()
        for node in self.nodes:
            if node not in self.ind:
                zero_ind.append(node)
        while len(zero_ind) > 0:
            node = zero_ind.pop()
            ret.append(node)
            if node not in self.edges:
                continue
            for q in self.edges[node]:
                if q not in ind_copy:
                    continue
                ind_copy[q] -= 1
                if ind_copy[q] == 0:
                    zero_ind.append(q)
        if len(self.nodes) == len(ret):
            return ret
        else:
            return None

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        group_items = {}
        group_graph = Graph()
        indv_group_graph = {}
        for idx in range(len(group)):
            if group[idx] == -1:
                group[idx] = m + idx
        for idx, group_idx in enumerate(group):
            if group_idx not in group_items:
                group_graph.add_node(group_idx)
                group_items[group_idx] = []
            group_items[group_idx].append(idx)
            if group_idx not in indv_group_graph:
                indv_group_graph[group_idx] = Graph()
            indv_group_graph[group_idx].add_node(idx)

        for idx, beforeItem in enumerate(beforeItems):
            for item in beforeItem:
                before_group = group[item]
                after_group = group[idx]
                if before_group != after_group:
                    group_graph.add_edge(before_group, after_group)
                else:
                    indv_group_graph[before_group].add_edge(item, idx)
        
        group_order = group_graph.topo_sort()
        if group_order is None:
            return []
        
        ret = []
        for g_idx in group_order:
            if g_idx not in indv_group_graph:
                ret += group_items[g_idx]
            else:
                temp = indv_group_graph[g_idx].topo_sort()
                if temp is None:
                    return []
                ret += temp

        return ret

s = Solution()
sol = s.sortItems(5, 3, [0,0,2,1,0], [[3],[],[],[],[1,3,2]])
print(sol)