"""
很好的dp优化问题
https://leetcode.com/problems/k-inverse-pairs-array/solutions/127746/k-inverse-pairs-array/

首先构造dp，考虑前n个数字，产生k个pair时，如果我们引入一个n+1，因为n+1比已知的所有数字都大，
把它放到i个位置，就一定产生了n-i个pair，所以可以
dp[n][k] = sum(dp[n-1][k-j]) (0<=j<=min(n-1, k))
此时答案是O(n^3)，可以构造一个前缀和
dp_sum[n][k] = sum(dp[n][i]) (0<=i<=k)
最后答案等于dp_sum[n][k] - dp_sum[n][k-1] (if k>0)
"""

class Solution:
    module = 10**9 + 7

    def dfs(self, n, k, dp_sum):
        if n == 0:
            return 0
        if k == 0:
            return 1
        if dp_sum[n][k] is None:
            ans = self.dfs(n-1, k, dp_sum)
            if k-n >= 0:
                ans += self.module - self.dfs(n-1, k-n, dp_sum)
            dp_sum[n][k] = (ans + self.dfs(n, k-1, dp_sum)) % self.module
        return dp_sum[n][k]

    def kInversePairs(self, n: int, k: int) -> int:
        dp_sum = [[None for _ in range(k+1)] for _ in range(n+1)]
        ans = self.dfs(n, k, dp_sum)
        if k>0:
            ans += self.module - self.dfs(n, k-1, dp_sum)
        return ans % self.module

s = Solution()
sol = s.kInversePairs(3, 1)
print(sol)