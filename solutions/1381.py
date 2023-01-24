"""
维护一个stack，额外有一种操作是可以往底下k个元素上加一个value。

额外维护一个inc，每次弹出top时考虑原值+inc值。由于此时inc对于top已失效，将inc[top]转移给inc[top-1]
"""

class CustomStack:
    def __init__(self, maxSize: int):
        self.inc = [0 for _ in range(maxSize)]
        self.values = [0 for _ in range(maxSize)]
        self.size = 0
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if self.size < self.maxSize:
            self.size += 1
            self.values[self.size-1] = x

    def pop(self) -> int:
        if self.size == 0:
            return -1
        top = self.size-1
        ret = self.values[top] + self.inc[top]
        if top > 0:
            self.inc[top-1] += self.inc[top]
        self.values[top] = 0
        self.inc[top] = 0
        self.size -= 1
        return ret

    def increment(self, k: int, val: int) -> None:
        if self.size > 0:
            k = min(k-1, self.size-1)
            self.inc[k] += val