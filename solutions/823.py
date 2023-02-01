"""
dp计数问题
"""

from typing import List
from typing import Optional
import math

module = 10**9+7

class Solution:
    def dfs(self, cur, arr, cache):
        if cur in cache:
            return cache[cur]
        if cur not in arr:
            return 0
        ans = 1 # just by itself
        for v in arr:
            if v != cur and cur > v and cur % v == 0 and (cur // v) in arr:
                temp = self.dfs(v, arr, cache) * self.dfs(cur // v, arr, cache)
                ans = (ans + temp) % module
        cache[cur] = ans % module
        return ans

    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr = set(arr)
        cache = {}
        ans = 0
        for num in arr:
            ans = (ans + self.dfs(num, arr, cache)) % module
        return ans % module

s = Solution()
sol = s.numFactoredBinaryTrees([46,144,5040,4488,544,380,4410,34,11,5,3063808,5550,34496,12,540,28,18,13,2,1056,32710656,31,91872,23,26,240,18720,33,49,4,38,37,1457,3,799,557568,32,1400,47,10,20774,1296,9,21,92928,8704,29,2162,22,1883700,49588,1078,36,44,352,546,19,523370496,476,24,6000,42,30,8,16262400,61600,41,24150,1968,7056,7,35,16,87,20,2730,11616,10912,690,150,25,6,14,1689120,43,3128,27,197472,45,15,585,21645,39,40,2205,17,48,136])
print(sol)