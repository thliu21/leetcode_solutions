from typing import List
from typing import Optional
import math
import heapq
from collections import Counter, deque

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        i = 0
        ans = 0
        n = len(prices)
        while i < n:
            if i == n-1:
                ans += 1
                break
            j = i+1
            while j < n and prices[j] == prices[j-1]-1:
                j += 1
            ll = j-1-i+1
            ans += (ll + 1) * ll // 2
            i = j
        return ans

s = Solution()
sol = s.getDescentPeriods([3,2,1,4])
print(sol)