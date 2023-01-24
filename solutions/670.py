"""
一个正整数，交换两个数字至多一次使其尽可能大

贪心，从左到右找到第一个上升的数字，然后从后面找一个最大的数字跟前面第一个比他小的交换。
如果后半部分有重复数字，优先使用数位靠后的。
"""

class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = [int(c) for c in str(num)]
        i = 0
        while i < len(nums)-1 and nums[i+1] <= nums[i]:
            i += 1
        if i == len(nums)-1:
            return num
        max_idx = len(nums)-1
        for i in range(len(nums)-1, i, -1):
            if nums[i] > nums[max_idx]:
                max_idx = i
        for i in range(0, i+1):
            if nums[i] < nums[max_idx]:
                nums[i], nums[max_idx] = nums[max_idx], nums[i]
                break
        ans = 0
        for num in nums:
            ans = ans*10 + num
        return ans

s = Solution()
sol = s.maximumSwap(99901)
print(sol)