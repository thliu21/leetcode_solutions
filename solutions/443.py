"""
SB题。。
"""

from collections import deque
from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        cur = 0
        while cur < len(chars):
            start = cur
            cur_char = chars[cur]
            count = 0
            while cur < len(chars) and cur_char == chars[cur]:
                count += 1
                cur += 1
            if count > 1:
                count_chars = list(str(count))
                while count > 1:
                    chars.pop(start+1)
                    count -= 1
                for idx, char in enumerate(count_chars):
                    chars.insert(start+1+idx, char)
                cur = start + len(count_chars) + 1
            else:
                cur = start + 1
        return len(chars)

s = Solution()
a = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
sol = s.compress(a)
print(a)
print(sol)