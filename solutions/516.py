"""
最长回文子序列
"""

class Solution:
    def dfs(self, s, i, j, dp):
        if dp[i][j] is not None:
            return dp[i][j]
        if i == j:
            return 1
        if j < i:
            return 0
        if s[i] == s[j]:
            dp[i][j] = self.dfs(s, i+1, j-1, dp) + 2
        else:
            dp[i][j] = max(self.dfs(s, i+1, j, dp), self.dfs(s, i, j-1, dp))
        return dp[i][j]

    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[None for _ in range(len(s))] for _ in range(len(s))]
        return self.dfs(s, 0, len(s)-1, dp)

s = Solution()
sol = s.longestPalindromeSubseq("bbbab")
print(sol)