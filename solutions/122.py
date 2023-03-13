"""
真正意义上的“贪心”。。。
"""

from typing import List
from typing import Optional
import math
import heapq
from collections import Counter, deque

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                ans += prices[i] - prices[i-1]
        return ans