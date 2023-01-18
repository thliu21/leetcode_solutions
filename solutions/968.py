"""
https://leetcode.com/problems/binary-tree-cameras/description/

二叉树，每个点上可以按一个相机，相机覆盖本点，父节点以及所有子节点。
求最少需要多少相机。

DP，对每个点求3种状态
1. 所有子节点都被覆盖，但自己没有被覆盖
2. 所有子节点都被覆盖，自己也被覆盖，但是自己没有装相机
3. 所有子节点都被覆盖，自己也被覆盖，且自己装了相机

状态转移O(1)，状态总量O(n)
"""

from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def dfs(self, node: TreeNode):
        if node is None:
            return 0, 0, 1<<30
        left = self.dfs(node.left)
        right = self.dfs(node.left)

        ret0 = left[1] + right[1]
        ret1 = min(left[2], min(right[1], right[2]), right[2], min(left[1], left[2]))
        ret2 = 1 + min(left) + min(right)

    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        ret = self.dfs(root)
        return min(ret[1], ret[2])
