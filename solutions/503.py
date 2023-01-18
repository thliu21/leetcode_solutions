"""
https://leetcode.com/problems/next-greater-element-ii/description/
对list中的每一个元素求他右侧第一个比他大的，数组可循环。

维护一个mono栈，从左向右，包含目前还未找到答案的元素。每找到一个新元素i就弹出栈顶所有比他小的元素j，并记i为j的答案。
"""

from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        size = len(nums)
        ret = [-1 for _ in nums]
        for idx, item in enumerate(nums + nums):
            while len(stack) > 0 and item > nums[stack[-1]]:
                prev_idx = stack.pop()
                ret[prev_idx] = item
            if idx < size:
                stack.append(idx)
        return ret

s = Solution()
sol = s.nextGreaterElements([1,2,3,4,3])
print(sol)