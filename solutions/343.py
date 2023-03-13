class Solution:
    def dfs(self, n, memo):
        if memo[n] is None:
            v = n-1
            for i in range(2, n):
                remain = n-i
                v = max(v, max(self.dfs(remain, memo), remain) * max(self.dfs(i, memo), i))
            memo[n] = v
        return memo[n]

    def integerBreak(self, n: int) -> int:
        memo = [None for _ in range(n+1)]
        memo[0] = 0
        memo[1] = 1
        memo[2] = 1
        return self.dfs(n, memo)

s = Solution()
sol = s.integerBreak(10)
print(sol)