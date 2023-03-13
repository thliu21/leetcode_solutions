from typing import List
from typing import Optional
import math
import heapq
from collections import Counter, deque

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        offset = 0
        if nums[-1]<nums[0]:
            l = 0
            r = len(nums)
            while l < r:
                mid = l + (r-l)//2
                if nums[mid] < nums[0]:
                    r = mid
                else:
                    l = mid+1
            offset = l
        l = 0
        r = len(nums)-1
        while l<r:
            mid = l + (r-l)//2
            v = nums[(mid+offset) % n]
            if v>=target:
                r = mid
            else:
                l = mid+1
        if nums[(l+offset)%n] == target:
            return (l+offset)%n
        else:
            return -1

s = Solution()
sol = s.search([1], 3)
print(sol)