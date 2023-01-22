"""
矩形图块分割问题
简单dp
"""

from typing import List
from typing import Optional

class Solution:
    module = 10**9 + 7

    def get_sum(self, sum, row, col):
        if row >= 0 and col >= 0:
            return sum[row][col]
        return 0

    def get_region(self, sum, r1, c1, r2, c2):
        return self.get_sum(sum, r2, c2) - self.get_sum(sum, r1-1, c2) - self.get_sum(sum, r2, c1-1) + self.get_sum(sum, r1-1, c1-1)

    def pre_sum(self, pizza):
        sum = [[0 for _ in range(len(pizza[0]))] for _ in range(len(pizza))]
        for i in range(len(pizza)):
            row_sum = [0 for _ in range(len(pizza[0]))]
            for j in range(len(pizza[0])):
                cur = 1 if pizza[i][j] == "A" else 0
                if j > 0:
                    cur += row_sum[j-1]
                row_sum[j] = cur
                pre_row_sum = cur
                if i > 0:
                    pre_row_sum += sum[i-1][j]
                sum[i][j] = pre_row_sum
        return sum
    
    def dfs(self, sum, dp, r, c, k, tr, tc):
        if r < 0 or c < 0 or r >= tr or c >= tc:
            # out of bound
            return 0
        if self.get_region(sum, r, c, tr-1, tc-1) < k: 
            # no enough apple
            return 0
        if k == 1 and self.get_region(sum, r, c, tr-1, tc-1) > 0: 
            # only one left
            return 1
        if dp[r][c][k] is None:
            ans = 0
            for nr in range(r+1, tr):
                if self.get_region(sum, r, c, nr-1, tc-1) > 0:
                    ans += self.dfs(sum, dp, nr, c, k-1, tr, tc) % self.module
            for nc in range(c+1, tc):
                if self.get_region(sum, r, c, tr-1, nc-1) > 0:
                    ans += self.dfs(sum, dp, r, nc, k-1, tr, tc) % self.module
            dp[r][c][k] = ans % self.module
        return dp[r][c][k]

    def ways(self, pizza: List[str], k: int) -> int:
        sum = self.pre_sum(pizza)
        tr = len(pizza)
        tc = len(pizza[0])
        dp = [[[None for _ in range(k+1)] for _ in range(len(pizza[0]))] for _ in range(len(pizza))]
        return self.dfs(sum, dp, 0, 0, k, tr, tc)

s = Solution()
sol = s.ways(["A..","AA.","..."], 1)
print(sol)