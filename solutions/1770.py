"""
二维DP
一开始错了几次是因为答案最小值设为了0，但实际上可能为负
"""

from typing import List
from typing import Optional
import math

class Solution:
    def dfs(self, l, r, nums, multipliers, dp):
        if l == 0 and r == 0:
            return 0
        if dp[l][r] is None:
            if l == 0:
                ans = self.dfs(l, r-1, nums, multipliers, dp) + multipliers[r+l-1]  * nums[-r]
            elif r == 0:
                ans = self.dfs(l-1, r, nums, multipliers, dp) + multipliers[r+l-1] * nums[l-1]
            else:
                ans = max(
                    self.dfs(l-1, r, nums, multipliers, dp) + multipliers[r+l-1] * nums[l-1],
                    self.dfs(l, r-1, nums, multipliers, dp) + multipliers[r+l-1]  * nums[-r]
                )
            dp[l][r] = ans
        return dp[l][r]

    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n = len(nums)
        m = len(multipliers)
        dp = [[None for _ in range(m+1)] for _ in range(m+1)]
        ans = -(1<<30)
        for left in range(m+1):
            ans = max(ans, self.dfs(left, m-left, nums, multipliers, dp))
        return ans

s = Solution()
sol = s.maximumScore([-5,-3,-3,-2,7,1], [-10,-5,3,4,6])
print(sol)