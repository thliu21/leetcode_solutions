class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr)-1
        while l < r:
            mid = (l+r) // 2
            print(l, mid, r)
            if arr[mid] < arr[mid+1]: # 可行条件
                l = mid+1
            else:
                r = mid
        return l