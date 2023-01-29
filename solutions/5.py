"""
二维可行性dp
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans_str = s[0]
        dp = [[True for _ in range(n+1)] for _ in range(n)]
        for i in range(n):
            dp[i][0] = True
            dp[i][1] = True
        for k in range(2, n+1):
            for i in range(0, n-k+1):
                dp[i][k] = s[i] == s[i+k-1] and dp[i+1][k-2]
                if dp[i][k]:
                    ans_str = s[i:i+k]
        return ans_str

s = Solution()
sol = s.longestPalindrome("bb")
print(sol)