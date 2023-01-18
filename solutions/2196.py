from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.val)

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {} # val => (treeNode, hasParent)

        for desc in descriptions:
            parent, child, isLeft = desc
            print(nodes)
            if child not in nodes:
                child_node = TreeNode(child)
                nodes[child] = (child_node, True)
            else:
                nodes[child] = (nodes[child][0], True)
            if parent not in nodes:
                parent_node = TreeNode(parent)
                nodes[parent] = (parent_node, False)
            if isLeft == 1:
                nodes[parent][0].left = nodes[child][0]
            else:
                nodes[parent][0].right = nodes[child][0]

        for val, node in nodes.items():
            if not node[1]:
                return node[0]

        return None

s = Solution()
sol = s.createBinaryTree([[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]])
print(sol)