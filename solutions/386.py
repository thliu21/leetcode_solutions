"""
水dfs
"""

from typing import List
from typing import Optional

class Solution:
    def dfs(self, n, cur):
        if cur > n:
            return []
        ret = []
        start = 0 if cur != 0 else 1
        end = 9
        for i in range(start, end+1):
            new = cur*10 + i
            if new <= n:
                ret.append(new)
                ret += self.dfs(n, new)
        return ret

    def lexicalOrder(self, n: int) -> List[int]:
        return self.dfs(n, 0)

s = Solution()
sol = s.lexicalOrder(2)
print(sol)