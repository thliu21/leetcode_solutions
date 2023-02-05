"""
dp 胡搞。。
"""

class Solution:
    def checkRecord(self, n: int) -> int:
        module = 10**9 + 7
        dp = [[[0 for _ in range(2)] for _ in range(3)] for _ in range(n)]
        dp[0][0][0] = 1 # P
        dp[0][0][1] = 1 # A
        dp[0][1][0] = 1 # L
        for i in range(1, n):
            dp[i][0][0] = dp[i-1][0][0] # Present all the way
            dp[i][0][0] += dp[i-1][1][0] + dp[i-1][2][0] # late for 1 or 2 days but Present
            dp[i][0][0] = dp[i][0][0] % module

            dp[i][0][1] = dp[i-1][0][1]
            dp[i][0][1] += dp[i-1][1][1] + dp[i-1][2][1] # present after late for 1 or 2 days
            dp[i][0][1] += dp[i-1][0][0] + dp[i-1][1][0] + dp[i-1][2][0] # absent after late for 0-2 days
            dp[i][0][1] = dp[i][0][1] % module

            dp[i][1][0] = dp[i-1][0][0] # late
            dp[i][1][1] = dp[i-1][0][1] # late with absent before
            dp[i][2][0] = dp[i-1][1][0] # late for 2nd time
            dp[i][2][1] = dp[i-1][1][1] # late for 2nd time with absent before
        ans = 0
        for l in range(3):
            for a in range(2):
                ans += dp[n-1][l][a] % module
        return ans % module

s = Solution()
sol = s.checkRecord(100000)
print(sol)
