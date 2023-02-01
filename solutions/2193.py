"""
https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/description/
贪心

https://www.youtube.com/watch?v=IUB4G_hp8ug
可以通过分类讨论证明，对于前n/2个元素，从尾部开始找到第一个元素，并将其交换至尾部，
然后对子字符串重复这个过程是最优答案。
"""

class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        s = list(s)
        n = len(s)
        count = 0
        ans = 0
        for i in range(n//2):
            j = n-1-count
            swap_count = 0
            while s[j] != s[i]:
                swap_count += 1
                j -= 1
            if i == j:
                ans += n//2-j
            else:
                while swap_count > 0:
                    s[j], s[j+1] = s[j+1], s[j]
                    swap_count -= 1
                    j += 1
                    ans += 1
                count += 1
        return ans

s = Solution()
sol = s.minMovesToMakePalindrome("awabb")
print(sol)
