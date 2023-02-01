"""
N方遍历，用斜率(y2-y1)/(x2-x1)判断
"""

from typing import List
from typing import Optional
import math

class Solution:
    def gcd(self, a, b):
        if a == 0:
            return b
        if b == 0:
            return a
        return self.gcd(b, a % b)

    def getSlope(self, x1, y1, x2, y2):
        dif_y = y2 - y1
        dif_x = x2 - x1
        if dif_x == 0:
            return (x1, 0)
        elif dif_y == 0:
            return (0, y1)
        d = self.gcd(dif_x, dif_y)
        return (dif_x // d, dif_y // d)

    def maxPoints(self, points: List[List[int]]) -> int:
        ans = 1
        for i, p in enumerate(points):
            same = 1
            count = {}
            max_points = 0
            for q in points[i+1:]:
                if p[0] == q[0] and p[1] == q[1]:
                    same += 1
                else:
                    slope = self.getSlope(p[0], p[1], q[0], q[1])
                if slope in count:
                    count[slope] += 1
                    max_points = max(max_points, count[slope])
                else:
                    count[slope] = 1
                    max_points = max(max_points, 1)
            ans = max(ans, same + max_points)
        return ans

s = Solution()
sol = s.maxPoints([[1,0],[0,0]])
print(sol)