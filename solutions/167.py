"""
two pointers模板题
"""

from typing import List
from typing import Optional
import math

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)-1
        while l < r:
            while l < r and nums[l] + nums[r] > target:
                r -= 1
            if nums[l] + nums[r] == target:
                return [l+1, r+1]
            l += 1
        return [0, 0]