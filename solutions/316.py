"""
https://leetcode.com/problems/remove-duplicate-letters/solution/
很好的字母序贪心问题
"""

from collections import Counter

class Solution:
    def removeDuplicateLetters_greedy(self, s: str) -> str:
        c = Counter(s)
        pos = 0
        for i in range(len(s)):
            if s[i] < s[pos]: 
                pos = i
            c[s[i]] -=1
            if c[s[i]] == 0: 
                break
        return s[pos] + self.removeDuplicateLetters(s[pos:].replace(s[pos], "")) if s else ''

    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        added = set()
        last_occurrence = {c: i for i, c in enumerate(s)}
        for idx, ch in enumerate(s):
            if ch not in added:
                while stack and stack[-1] > ch and last_occurrence[stack[-1]] > idx:
                    added.remove(stack.pop())
                added.add(ch)
                stack.append(ch)
        return "".join(stack)

s = Solution()
sol = s.removeDuplicateLetters("bbcaac")
print(sol)