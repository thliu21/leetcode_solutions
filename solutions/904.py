from typing import List
from typing import Optional
import math
import heapq
from collections import Counter, deque

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        n = len(fruits)
        window = {fruits[0]: 1}
        ans = 1
        for r in range(1, n):
            if fruits[r] in window:
                window[fruits[r]] += 1
            else:
                window[fruits[r]] = 1
            while len(window.keys()) > 2 and l < r:
                window[fruits[l]] -= 1
                if window[fruits[l]] == 0:
                    del window[fruits[l]]
                l += 1
            ans = max(ans, r-l+1)
        return ans

s = Solution()
sol = s.totalFruit([0,1,2,2])
print(sol)