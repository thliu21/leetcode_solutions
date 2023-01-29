"""
可行性背包

注意细节处理，对于一个一直可达的值，分情况讨论
- 如果cost已经超过target，那就不再考虑加topping，因为必然导致答案距离target更大
- 如果cost+topping已经超过了target，就不再考虑topping*2，因为必然导致答案距离target更大
结果出答案的时候要注意细节
"""

from collections import deque
from typing import List, Set

class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        possible_costs = set(baseCosts)
        for topping in toppingCosts:
            new_set = set()
            for cost in possible_costs:
                if cost == target:
                    return target
                new_set.add(cost)
                if cost < target:
                    new_set.add(cost + topping)
                    if cost + topping < target:
                        new_set.add(cost + topping * 2)
            possible_costs = new_set
        possible_costs = list(possible_costs)
        possible_costs.sort()
        possible_costs.reverse()
        ans = possible_costs[0]
        print(possible_costs)
        for cost in possible_costs:
            if cost == target:
                return target
            diff = abs(target - cost)
            if abs(ans-target) >= diff:
                ans = cost
        return ans

s = Solution()
sol = s.closestCost([4], [9], 9)
print(sol)
