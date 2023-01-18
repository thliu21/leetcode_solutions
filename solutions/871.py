"""
https://leetcode.com/problems/minimum-number-of-refueling-stops/description/
从0出发，起始有n单位的油，一维路上有若干加油站，每个加油站有距离和油量给定，求最少加多少次可以到距离t

https://leetcode.com/problems/minimum-number-of-refueling-stops/solutions/149817/minimum-number-of-refueling-stops/
最初想法是设一个dp[i][j]表示到达第i个加油站，加了j次油时，最多能剩多少油，n^3会TLE。
题解有两个算法
1. 可以设一个dp[i]表示在加了i次油的情况下，最多可以跑多远。
从头开始考虑每一个加油站，对于每个加油站i，考虑之前加到i-1到0次油，取最大值
最后看dp[i] > t 且i最小。O(n^2)
2. 贪心，其实和dp类似。从头开始考虑每个加油站，一直开到没有油，维护一个之前加油站的油量，从最大的加油站开始取。
如果取尽了还无法到达下一站说明无解。一直到终点即可。O(nlogn)

感觉贪心思路比较直接，思路更好。
"""

from typing import List
from typing import Optional
import heapq

class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        pq = []
        stations.append((target, 1<<30))

        ans = 0
        prev_loc = 0
        tank = startFuel
        for loc, gas in stations:
            tank -= loc - prev_loc
            while len(pq) and tank < 0:
                tank += -heapq.heappop(pq)
                ans += 1
            if tank < 0:
                return -1
            heapq.heappush(pq, -gas)
            prev_loc = loc
        return ans

s = Solution()
sol = s.minRefuelStops(100, 10, [[10,60],[20,30],[30,30],[60,40]])
print(sol)