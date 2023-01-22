"""
一个数组，每个数字都是1<=i<=n，每个数字一定出现了1或2次，要求n时间内求出有那些数字是重复的，不能开数组。

脑筋急转弯。。用负号原地标记哪个位置出现过，扫两趟。
"""

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        size = len(nums)
        for i in range(size):
            nums[abs(nums[i])-1] *= -1
        for i in range(size):
            if nums[abs(nums[i])-1] > 0:
                ans.append(abs(nums[i]))
                nums[abs(nums[i])-1] *= -1
        return ans
 
s = Solution()
sol = s.findDuplicates([4,3,2,7,8,2,3,1])
print(sol)