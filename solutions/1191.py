"""
https://leetcode.com/problems/k-concatenation-maximum-sum/description/

分情况讨论
- 由单一节出答案 maxSubArray
- 由两个相连的节出答案 max_suf_sum + max_pre_sum
- 由全体相连出答案 max_suf_sum + max_pre_sum + (k-2)*sum(arr)

"""

from typing import List
from typing import Optional

class Solution:
    def maxSubArray(self, nums: List[int]):
        l = r = 0
        cur = nums[0]
        ans = nums[0]
        for num in nums[1:]:
            cur = max(num, cur + num)
            ans = max(ans, cur)
        return ans

    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        mod = 10**9 + 7

        size = len(arr)
        pre_sum = [0 for _ in arr]
        pre_sum[0] = arr[0]
        max_pre_sum = max(0, arr[0])
        for i in range(1, size):
            pre_sum[i] = pre_sum[i-1] + arr[i]
            max_pre_sum = max(max_pre_sum, pre_sum[i])
        
        max_suf_sum = pre_sum[size-1]
        for i in range(size):
            max_suf_sum = max(max_suf_sum, pre_sum[size-1] - pre_sum[i])

        ans = 0
        ans = max(ans, self.maxSubArray(arr))

        if k > 1:
            max2 = max_suf_sum + max_pre_sum
            print(max_pre_sum, max_suf_sum)
            ans = max(ans, max2)
            ans = max(ans, max2 + (k-2)*pre_sum[size-1])
        
        return ans % mod
        
s = Solution()
sol = s.kConcatenationMaxSum([1,2], 3)
print(sol)