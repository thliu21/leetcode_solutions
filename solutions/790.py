"""
组合量问题，简单dp
"""

class Solution:
    def dfs(self, dp, n, state):
        module = 10**9 + 7
        if n == 0:
            if state == 3:
                return 1
            else:
                return 0
        if n < 0:
            return 0
        if dp[n][state] is not None:
            return dp[n][state]
        ret = 0
        if state == 3:
            ret = self.dfs(dp, n-1, 3) + self.dfs(dp, n-2, 3) + self.dfs(dp, n-1, 1) + self.dfs(dp, n-1, 2)
        elif state == 2:
            ret = self.dfs(dp, n-1, 1) + self.dfs(dp, n-2, 3)
        elif state == 1:
            ret = self.dfs(dp, n-1, 2) + self.dfs(dp, n-2, 3)
        dp[n][state] = ret % module
        return ret

    def numTilings(self, n: int) -> int:
        module = 10**9 + 7
        dp = [[None for _ in range(4)] for _ in range(n+1)]
        return self.dfs(dp, n, 3) % module