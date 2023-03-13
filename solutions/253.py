"""
堆贪心
一开始以为只要排序扫描，但问题是无法track每个rooms的结束时间。
还有一种做法是按开始时间和结束时间分别排序，但是感觉没有用heap直观。
"""

from typing import List
from typing import Optional
import math
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        rooms = []
        heapq.heappush(rooms, intervals[0][1])
        for interval in intervals[1:]:
            if rooms[0] <= interval[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, interval[1])
        return len(rooms)

s = Solution()
sol = s.minMeetingRooms([[7,10],[2,4]])
print(sol)