"""
水题，裸dfs
"""

from typing import List

class Solution:
    def dfs(self, items, cur_item_idx, cur_set, answers):
        if cur_item_idx == len(items):
            answers.append(cur_set[:])
            return
        for count in range(items[cur_item_idx][1]+1):
            cur_set += [items[cur_item_idx][0] for _ in range(count)]
            self.dfs(items, cur_item_idx+1, cur_set, answers)
            for _ in range(count):
                cur_set.pop()

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        item_counts = {}
        for num in nums:
            if num not in item_counts:
                item_counts[num] = 0
            item_counts[num] += 1
        item_counts = list(item_counts.items())
        answers = []
        self.dfs(item_counts, 0, [], answers)
        return answers


s = Solution()
sol = s.subsetsWithDup([0])
print(sol)