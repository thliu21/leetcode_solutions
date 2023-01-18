from typing import List

class Solution:
    def mctFromLeafValues(self, arr):
        ans = 0
        while len(arr) > 1:
            minIndex = arr.index(min(arr))
            if 0 < minIndex < len(arr) - 1:
                ans += min(arr[minIndex - 1], arr[minIndex + 1]) * arr[minIndex]
            else: 
                ans += arr[1 if minIndex == 0 else minIndex - 1] * arr[minIndex]
            arr.pop(minIndex)
        return ans

s = Solution()
sol = s.mctFromLeafValues([6,2,4])
print(sol)