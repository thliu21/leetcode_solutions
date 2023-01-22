"""
水题
"""

class Solution:
    def dfs(self, node):
        if node is None:
            return 0, 0
        dfs_l = self.dfs(node.left)
        dfs_r = self.dfs(node.right)
        ret0 = 1
        if node.left is not None and node.left.val == node.val + 1:
            ret0 = max(ret0, dfs_l[0] + 1)
        if node.right is not None and node.right.val == node.val + 1:
            ret0 = max(ret0, dfs_r[0] + 1)
        return ret0, max(ret0, dfs_l[1], dfs_r[1])

    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        ret = self.dfs(root)
        return max(ret[0], ret[1])