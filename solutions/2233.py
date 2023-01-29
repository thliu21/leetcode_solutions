"""
堆贪心
"""

import heapq

class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        module = 10**9 + 7
        heapq.heapify(nums)
        while k > 0:
            value = heapq.heappop(nums)
            heapq.heappush(nums, value + 1)
            k -= 1
        ans = 1
        for num in nums:
            ans = (ans * num) % module
        return ans % module