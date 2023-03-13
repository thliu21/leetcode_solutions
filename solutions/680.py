class Solution:
    def valid(self, s, i, j) -> bool:
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        valid = True
        for i in range(n // 2 + 1):
            j = n - i - 1
            if s[i] != s[j]:
                valid = False
                break
        if valid:
            return True
        return self.valid(s, i, j-1) or self.valid(s, i+1, j)

s = Solution()
sol = s.validPalindrome("abca")
print(sol)