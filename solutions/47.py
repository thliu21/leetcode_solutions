"""
水题
"""

from typing import List
from typing import Optional
import math

class Solution:
    def dfs(self, count, remain) -> List[List[int]]:
        if remain == 0:
            return [[]]
        ans = []
        for k in count.keys():
            if count[k] <= 0:
                continue
            count[k] -= 1
            ret = self.dfs(count, remain-1)
            for r in ret:
                ans.append([k] + r)
            count[k] += 1
        return ans


    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        return self.dfs(count, len(nums))

s = Solution()
sol = s.permuteUnique([1, 2, 3])
print(sol)