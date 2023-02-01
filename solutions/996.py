"""
DFS
"""

from typing import List
from typing import Optional
import math

class Solution:
    def perfectSquare(self, n):
        a = math.sqrt(n)
        return (a - int(a)) < 1e-6

    def dfs(self, counts, last, remain):
        if remain == 0:
            return 1
        ret = 0
        if last is not None:
            for k, v in counts.items():
                if v > 0 and self.perfectSquare(k+last):
                    counts[k] -= 1
                    ret += self.dfs(counts, k, remain-1)
                    counts[k] += 1
        else:
            for k, v in counts.items():
                if v > 0:
                    counts[k] -= 1
                    ret += self.dfs(counts, k, remain-1)
                    counts[k] += 1
        return ret

    def numSquarefulPerms(self, nums: List[int]) -> int:
        counts = {}
        n = len(nums)
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        ret = self.dfs(counts, None, n)
        return ret

s = Solution()
sol = s.numSquarefulPerms([2,2,2])
print(sol)