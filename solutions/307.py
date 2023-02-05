"""
树状数组模板题
"""

from typing import List
from typing import Optional
import math

class BIT:
    def __init__(self, size):
        self.BIT = [0] * (size+1)
            
    def update(self, i: int, delta: int) -> None:
        i += 1
        while i < len(self.BIT):
            self.BIT[i] += delta
            i += (i&-i)

    def updateTo(self, i: int, val: int) -> None:
        cur = self.query(i)
        if i > 0:
            cur -= self.query(i-1)
        self.update(i, val-cur)
        
    def query(self, i):
        i += 1
        ans = 0
        while i > 0:
            ans += self.BIT[i]
            i -= (i&-i)
        return ans

class NumArray:

    def __init__(self, nums: List[int]):
        self.bit = BIT(len(nums))
        for i in range(len(nums)):
            self.bit.updateTo(i, nums[i])

    def update(self, index: int, val: int) -> None:
        self.bit.updateTo(index, val)

    def sumRange(self, left: int, right: int) -> int:
        ans = self.bit.query(right)
        if right > 0:
            ans -= self.bit.query(left-1)
        return ans