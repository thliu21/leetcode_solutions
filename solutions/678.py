"""
https://leetcode.com/problems/valid-parenthesis-string/description/

可以设计成一个dp，dp[i]包含一个set表示到第i个字符，剩余某个数量的open是否可能达到。
最后是N立方的复杂度。
贪心的思路其实是对于第三维的压缩，因为*是+1，-1或者0，这个set一定是连续的，可以只考虑最高点和最低点
然后O(n)遍历一次即可
"""

class Solution():
    def checkValidString(self, s):
        lo = hi = 0
        for c in s:
            lo += 1 if c == '(' else -1
            hi += 1 if c != ')' else -1
            if hi < 0: break
            lo = max(lo, 0)
        return lo == 0