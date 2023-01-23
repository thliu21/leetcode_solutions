"""
数学题
重点是 (p-q)%k = 0 ==> p%k = q%k
"""

from typing import List
from typing import Optional

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        pre_sum = [0 for _ in nums]
        pre_sum[0] = nums[0]
        for i in range(1, len(nums)):
            pre_sum[i] = pre_sum[i-1] + nums[i]
            if pre_sum[i] % k == 0:
                return True
        existed = {}

        for i in range(0, len(nums)):
            mod = pre_sum[i] % k
            if mod in existed:
                index = existed[mod]
                if (index+1) < i:
                    return True
            else:
                existed[mod] = i
        
        return False

s = Solution()
sol = s.checkSubarraySum([1,2,3], 5)
print(sol)