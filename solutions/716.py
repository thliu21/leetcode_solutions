"""
lazy 维护heap和stack
有一个缺陷是，removed会越变越大，需要引入一些清理removed的逻辑
"""

import heapq as hp

class MaxStack:

    def __init__(self):
        self.removed = set()
        self.heap = []
        self.cnt = 0
        self.stack = []

    def push(self, x: int) -> None:
        hp.heappush(self.heap, (-x, -self.cnt))
        self.stack.append((x, self.cnt))
        self.cnt += 1

    def pop(self) -> int:
        while self.stack and self.stack[-1][1] in self.removed:
            self.stack.pop()
        num, idx = self.stack.pop()
        self.removed.add(idx)
        return num

    def top(self) -> int:
        while self.stack and self.stack[-1][1] in self.removed:
            self.stack.pop()
        return self.stack[-1][0]

    def peekMax(self) -> int:
        while self.heap and -self.heap[0][1] in self.removed:
            hp.heappop(self.heap)
        return -self.heap[0][0]

    def popMax(self) -> int:
        while self.heap and -self.heap[0][1] in self.removed:
            hp.heappop(self.heap)
        num, idx = hp.heappop(self.heap)
        self.removed.add(-idx)
        return -num



# Your MaxStack object will be instantiated and called as such:
stk = MaxStack()
stk.push(5)
stk.push(1)
stk.push(5)
print(stk.top())
print(stk.popMax())
print(stk.top())
print(stk.peekMax())
print(stk.pop())
print(stk.top())