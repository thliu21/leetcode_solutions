"""
n个正整数，每次可以把一个数字+1，问最少需要多少次可以让所有数字unique

贪心，从小到大排序，以最小代价往上加
"""

from typing import List
from typing import Optional

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        max_v = nums[0]
        for i in range(1, len(nums)):
            if nums[i] <= max_v:
                max_v += 1
                ans += max_v - nums[i]
            else:
                max_v = nums[i]
        return ans
        

s = Solution()
sol = s.minIncrementForUnique([3,2,1,2,1,7])
print(sol)