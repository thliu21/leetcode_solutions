"""
https://leetcode.com/problems/maximum-subarray/description/
经典题，求数列最大子段，数字有正负
对于一个负数，留下他的条件是带他一起收益为正。
从左向右考虑，一直加，如果遇到一个负数并且当前加和为负时，抛弃之前的加和。
"""

from typing import List
from typing import Optional

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = nums[0]
        ans = nums[0]
        for num in nums[1:]:
            cur = max(num, cur + num)
            ans = max(ans, cur)
        return ans

s = Solution()
sol = s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(sol)