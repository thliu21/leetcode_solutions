"""
n个房间，m个会议，按房间index开始安排会议，如果没有空房间就推迟到第一个结束的房间。
求哪一个房间开了最多的会。

按会议开始时间排序，两个堆维护空房间和在用的房间。对每个会议，先弹出所有已经结束的房间。
如果有可用的就用，没有的话就弹出结束时间最早的房间加钟，再push回堆，记录会议次数。
"""

from typing import List
import heapq as hq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        meeting_count = [0 for _ in range(n)]
        free_rooms = [i for i in range(n)]
        hq.heapify(free_rooms)
        in_use_rooms = [] # (end_t, room_number)

        for meeting in meetings:
            m_start = meeting[0]
            m_end = meeting[1]
            while len(in_use_rooms) > 0:
                end_t, room_num = in_use_rooms[0]
                if end_t <= m_start:
                    hq.heappush(free_rooms, room_num)
                    hq.heappop(in_use_rooms)
                else:
                    break
            if len(free_rooms) > 0:
                room_num = hq.heappop(free_rooms)
                meeting_count[room_num] += 1
                hq.heappush(in_use_rooms, (m_end, room_num))
            else:
                end_t, room_num = hq.heappop(in_use_rooms)
                meeting_count[room_num] += 1
                hq.heappush(in_use_rooms, (end_t + (m_end-m_start), room_num))
        return meeting_count.index(max(meeting_count))

s = Solution()
sol = s.mostBooked(3, [[1,20],[2,10],[3,5],[4,9],[6,8]])
print(sol)