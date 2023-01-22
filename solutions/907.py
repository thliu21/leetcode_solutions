"""
https://leetcode.com/problems/sum-of-subarray-minimums/description/
取所有连续子序列，求所有子序列中最小数值的和

单调栈，对于每个点i求其左侧和右侧分别最小的点l, r，在这个范围内，
所有以i为中心的子序列一定是以i为最小值，计入答案
特殊情况为，如果有重复的数字，这种做法会重复计算。
解决办法是考虑左侧的时候用>，考虑右侧时用>=。
"""

from typing import List
from typing import Optional

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10**9 + 7

        left_smallest = [-1 for _ in arr]
        right_smallest = [-1 for _ in arr]
        stack = []

        for idx, num in enumerate(arr):
            while len(stack) > 0 and arr[stack[-1]] >= num:
                top = stack.pop()
                right_smallest[top] = idx
            stack.append(idx)

        stack = []
        for idx in range(len(arr)-1, -1, -1):
            while len(stack) > 0 and arr[stack[-1]] > arr[idx]:
                top = stack.pop()
                left_smallest[top] = idx
            stack.append(idx)

        ans = 0
        for idx in range(len(arr)):
            l = 0 if left_smallest[idx] == -1 else left_smallest[idx] + 1
            r = len(arr)-1 if right_smallest[idx] == -1 else right_smallest[idx] - 1
            # print(arr[idx], l, r)
            ans += (arr[idx] * (r-idx+1) * (idx-l+1)) % mod

        return ans % mod

s = Solution()
sol = s.sumSubarrayMins([3,1,2,4])
print(sol)