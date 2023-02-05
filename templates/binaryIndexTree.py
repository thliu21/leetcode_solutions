# https://leetcode.com/problems/range-sum-query-mutable/solutions/814179/python-fenwick-tree-bit-and-segment-tree-o-nlogn-short-concise/

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

a = [1, 2, 3, 4, 5, 6, 7]
bit = BIT(len(a))
for idx, v in enumerate(a):
    bit.update(idx, v)
print(bit.query(4))
bit.updateTo(0, -3)
print(bit.query(5))