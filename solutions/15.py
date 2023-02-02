"""
two sum延伸，先定住一个i然后对i+1~n进行two sum
"""

from typing import List
from typing import Optional
import math

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)-1
        ans = []
        while l < r:
            sum = nums[l] + nums[r]
            if sum < target:
                l += 1
            elif sum > target:
                r -= 1
            else:
                ans.append([nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
        return ans

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        i = 0
        while i < len(nums):
            pairs = self.twoSum(nums[i+1:], -nums[i])
            for pair in pairs:
                ans.append([nums[i], pair[0], pair[1]])
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            i += 1
        return ans

s = Solution()
sol = s.threeSum([-1,0,1,2,-1,-4])
print(sol)