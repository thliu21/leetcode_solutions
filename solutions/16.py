from typing import List
from typing import Optional
import math
import heapq
from collections import Counter, deque

class Solution:
    def slidingWindow(self, goal, idx, nums):
        l = idx
        r = len(nums)-1
        closest = 1<<31
        while l < r:
            temp = nums[l]+nums[r]
            diff = abs(goal-temp)
            if diff == 0:
                return temp
            if diff < abs(closest-goal):
                closest = temp
            if temp > goal:
                r -= 1
            else:
                l += 1
        return closest

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = 1<<31
        for idx, num in enumerate(nums):
            temp = self.slidingWindow(target - num, idx+1, nums)
            if abs(target - (temp+num)) < abs(target - closest):
                closest = temp+num
        return closest

s = Solution()
sol = s.threeSumClosest([4,0,5,-5,3,3,0,-4,-5], -2)
print(sol)