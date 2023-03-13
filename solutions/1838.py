"""
- 排序之后，对于每个数字，贪心地向前找尽可能多的元素使得总和差小于k，可以二分，这样总共nlogn。
- 也可以sliding window，其实更好一些，右侧一直加，如果遇到k不够用了就抛弃前面的元素。不过因为排序是nlogn，所以理论上没有变快
"""

from typing import List
from typing import Optional
import math
import heapq
from collections import Counter, deque

class Solution:
    def getSum(self, pre_sum, i, j):
        ret = pre_sum[j]
        if i > 0:
            ret -= pre_sum[i-1]
        return ret

    def find(self, nums, pre_sum, idx, k):
        if idx == 0:
            return 0
        l = 0
        r = idx
        val = nums[idx]
        while l<r:
            mid = l+(r-l)//2
            needed = mid * val - self.getSum(pre_sum, idx-mid, idx-1)
            if needed > k:
                r = mid
            else:
                l = mid+1
        if l * val - self.getSum(pre_sum, idx-l, idx-1) <= k:
            return l
        return l-1
            

    def maxFrequency_bsearch(self, nums: List[int], k: int) -> int:
        nums.sort()
        pre_sum = [0 for _ in range(len(nums))]
        pre_sum[0] = nums[0]
        for i in range(1, len(nums)):
            pre_sum[i] = pre_sum[i-1] + nums[i]
        ans = 1
        for i in range(0, len(nums)):
            ans = max(ans, 1 + self.find(nums, pre_sum, i, k))
        return ans

    # sliding window
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        cnt = 0
        ans = 1
        sum = 0
        for r in range(len(nums)):
            sum += nums[r]
            while (r-l+1)*nums[r] - sum > k:
                sum -= nums[l]
                l += 1
            ans = max(ans, (r-l+1))
        return ans

s = Solution()
sol = s.maxFrequency([1, 2,4], 5)
print(sol)
