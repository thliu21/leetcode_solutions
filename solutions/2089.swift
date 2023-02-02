"""
二分模板题
"""

class Solution {
    func targetIndices(_ nums: [Int], _ target: Int) -> [Int] {
        var arr = nums.sorted()
        var l = 0
        var r = arr.count
        while l < r {
            let mid = l + (r-l)/2
            if arr[mid] >= target {
                r = mid
            } else {
                l = mid + 1
            }
        }
        var ans = [Int]()
        while l < arr.count && arr[l] == target {
            ans.append(l)
            l += 1
        }
        return ans
    }
}

let s = Solution()
let sol = s.targetIndices([1,2,5,2,3], 2)
print(sol)