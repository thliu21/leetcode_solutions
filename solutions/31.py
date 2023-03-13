from typing import List
from typing import Optional
import math
import heapq
from collections import Counter, deque

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        i = n-1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i == 0:
            nums.reverse()
            return
        i -= 1
        j = n-1
        while nums[i]>=nums[j]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        l = i+1
        r = n-1
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
            r-=1

nums = [1, 2, 4, 9, 8, 7, 6, 5, 3]
print(nums)
s = Solution()
s.nextPermutation(nums)
print(nums)
