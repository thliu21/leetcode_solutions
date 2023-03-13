from typing import List
from typing import Optional
import math
import heapq
from collections import Counter, deque

class Solution:
    def catchMaximumAmountofPeople(self, team: List[int], dist: int) -> int:
        ones = deque([idx for idx, t in enumerate(team) if t == 1])
        ans = 0
        for idx, t in enumerate(team):
            if len(ones) == 0:
                break
            if t == 0:
                while ones and ones[0] + dist < idx:
                    ones.popleft()
                if abs(ones[0] - idx) <= dist:
                    ans += 1
                    ones.popleft()
        return ans

s = Solution()
sol = s.catchMaximumAmountofPeople([0,1,0,1,0], 3)
print(sol)