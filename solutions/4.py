from typing import List
from typing import Optional
import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        intMax = 1<<30
        intMin = -intMax
        n = len(nums1)
        m = len(nums2)
        if n > m:
            return self.findMedianSortedArrays(nums2, nums1)

        # k 表示一共需要找的元素，是总数量的一半
        k = (n+m+1)//2
        ll = 0
        rr = n
        while ll < rr:
            m1 = ll + (rr-ll)//2 # 从第一个数组中拿出m1个元素
            m2 = k - m1 # 从第二个数组中取剩下所需要的元素
            # 如果nums1的第m1+1个元素比nums2中的最大元素小
            # 表示nums2中一定有一个或多个元素不应该出现
            # 说明在nums1中的元素拿少了，m1应该变大
            if nums1[m1] < nums2[m2-1]:
                ll = m1+1
            else:
                rr = m1

        p = ll
        q = k-ll
        # 从nums1和nums2中拿出p和q个元素，可能有一个数组完全没用上
        c1 = max(intMin if p<=0 else nums1[p-1], intMin if q<=0 else nums2[q-1])
        if (n+m) % 2 == 1: # 奇数个元素时这就是答案
            return c1

        # 偶数时就再往后找一个
        c2 = min(intMax if p>=n else nums1[p], intMax if q>=m else nums2[q])
        return (c1+c2) / 2

s = Solution()
sol = s.findMedianSortedArrays([1, 2, 3, 4, 5, 7], [8, 11, 13])
print(sol)