"""
水题，注意用deque
"""

from collections import deque
from typing import List

class HitCounter:
    WINDOW_SIZE = 300

    def __init__(self):
        self.queue = deque()

    def hit(self, timestamp: int) -> None:
        self.queue.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while len(self.queue):
            if timestamp - self.queue[0] >= self.WINDOW_SIZE:
                self.queue.popleft()
            else:
                break
        return len(self.queue)

hitCounter = HitCounter()
hitCounter.hit(1)
hitCounter.hit(2)
hitCounter.hit(3)
print(hitCounter.getHits(4))
hitCounter.hit(300)
print(hitCounter.getHits(300))
print(hitCounter.getHits(301))