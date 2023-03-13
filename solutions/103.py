class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List
from typing import Optional
import math
import heapq
from collections import Counter, deque

class Solution:
    def dfs(self, root):
        if root is None:
            return
        self.dfs(root.left)
        print(root.val)
        self.dfs(root.right)

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.dfs(root)
        level = 0
        queue = deque([root])
        ans = []
        while len(queue) > 0:
            level += 1
            nextLevel = deque([])
            curLevel = []
            while len(queue) > 0:
                head = queue.popleft()
                curLevel.append(head.val)
                if head.left:
                    nextLevel.append(head.left)
                if head.right:
                    nextLevel.append(head.right)
            if level % 2 == 0:
                curLevel.reverse()
            ans.append(curLevel)
            queue = nextLevel
        return ans

s = Solution()
node3 = TreeNode(3)
node9 = TreeNode(9)
node20 = TreeNode(20)
node15 = TreeNode(15)
node7 = TreeNode(7)
node3.left = node9
node3.right = node20
node20.left = node15
node20.right = node7
sol = s.zigzagLevelOrder(node3)
print(sol)