"""
水题，裸判有根树某点所有子孙
"""

from typing import List

class Node:
    def __init__(self, pid) -> None:
        self.pid = pid
        self.child_node = []

    def add_child(self, node):
        self.child_node.append(node)

    def find_all_children(self) -> List[int]:
        ret = [self.pid]
        for node in self.child_node:
            ret += node.find_all_children()
        return ret

class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        nodes = {0: Node(0)}
        for p in pid:
            nodes[p] = Node(p)
        for p, pp in list(zip(pid, ppid)):
            nodes[pp].add_child(nodes[p])
        return nodes[kill].find_all_children()

s = Solution()
sol = s.killProcess([1,3,10,5], [3,0,5,3], 3)
print(sol)