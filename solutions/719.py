"""
二分模板
https://leetcode.com/problems/find-k-th-smallest-pair-distance/solutions/127408/find-k-th-smallest-pair-distance/
排序整个序列，可以设计一个check(a)表示是否有至少k个差值，可以通过sliding window算出
然后二分check(a)的单调性即可。
"""

from typing import List
from typing import Optional
import math

class Solution:
    def check(self, nums, k, guess):
        l = count = 0
        for r, v in enumerate(nums):
            while v - nums[l] > guess:
                l += 1
            count += r-l
        return count >= k

    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        r = nums[-1]-nums[0]
        while l<r:
            mid = l + (r-l) // 2
            if self.check(nums, k, mid):
                r = mid
            else:
                l = mid + 1
        return l

s = Solution()
sol = s.smallestDistancePair([1,3,1], 1)
print(sol)