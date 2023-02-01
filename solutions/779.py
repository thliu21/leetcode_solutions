class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        ans = True
        k -= 1
        while n > 0:
            if k % 2 == 1:
                ans = not ans
            k = k // 2
            n -= 1
        if ans:
            return 0
        else:
            return 1