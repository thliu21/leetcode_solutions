"""
二分模板题
"""

from collections import deque
from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr)-1
        while l < r:
            mid = (l+r) // 2
            print(l, mid, r)
            if arr[mid] < arr[mid+1]:
                l = mid+1
            else:
                r = mid
        return l

s = Solution()
sol = s.peakIndexInMountainArray([3, 4, 5, 6, 7, 8, 9, 6, 3, 2, 1, 0])
print(sol)