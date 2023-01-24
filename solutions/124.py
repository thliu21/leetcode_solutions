"""
https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

简单树上dfs，思路类似array最大区间，如果子支为负且当前值为负时直接抛弃
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root):
        inf = 1<<30
        if root is None:
            return -inf, -inf
        ret0 = root.val
        ret1 = root.val

        dfs_left = self.dfs(root.left)
        dfs_right = self.dfs(root.right)

        ret0 = max(
            dfs_left[0] + root.val, 
            dfs_right[0] + root.val, 
            root.val
        )

        ret1 = max(
            ret0,
            dfs_left[0] + dfs_right[0] + root.val,
            dfs_left[1],
            dfs_right[1]
        )
        return ret0, ret1

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = self.dfs(root)
        return ans[1]