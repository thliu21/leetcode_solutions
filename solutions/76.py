"""
https://leetcode.com/problems/minimum-window-substring/description/

经典sliding window。
总体来说用[l,r)表示window会比较容易，r表示下一个可以加入window的元素，可以在代码里少些很多+1
"""

class Solution:
    def all_char(self, cur_remain_chars):
        for k, v in cur_remain_chars.items():
            if v > 0:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        ans = None
        n = len(s)
        cur_ans_len = 0
        m = len(t)

        if n == 1:
            if s == t:
                return s
            else:
                return ""
    
        if s == t:
            return s

        cur_remain_chars = {}
        for c in t:
            if c in cur_remain_chars:
                cur_remain_chars[c] += 1
            else:
                cur_remain_chars[c] = 1
        
        l = r = 0 # [l, r)
        while 1:
            while r < n and not self.all_char(cur_remain_chars):
                if s[r] in cur_remain_chars:    
                    cur_remain_chars[s[r]] -= 1
                r += 1

            # print("+r", l, r, s[l: r], cur_remain_chars)

            if self.all_char(cur_remain_chars):
                if ans == None or (r-l) < cur_ans_len:
                    ans = s[l: r]
                    cur_ans_len = (r-l)
            else:
                break

            while l < r:
                if s[l] in cur_remain_chars:
                    cur_remain_chars[s[l]] += 1
                l += 1
                if self.all_char(cur_remain_chars):
                    if ans == None or (r-l) < cur_ans_len:
                        ans = s[l: r]
                        cur_ans_len = (r-l)
                else:
                    break

            # print("+l", l, r, s[l: r], cur_remain_chars)
            
            while l < r:
                if s[l] not in cur_remain_chars:
                    l += 1
                else:
                    break
            # print("+clear", l, r, s[l: r], cur_remain_chars)
            if len(ans) == m:
                return ans

        if ans is None:
            return ""
        else:
            return ans

s = Solution()
sol = s.minWindow("ab", "b")
print(sol)