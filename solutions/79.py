"""

"""

from typing import List
from typing import Optional
import math

class Solution:
    def dfs(self, i, j, row, col, board, word):
        if len(word) == 0:
            return True
        if i < 0 or j < 0 or i >= row or j >= col:
            return False
        if board[i][j] != word[0]:
            return False
        temp = board[i][j]
        board[i][j] = "$"
        m_x = (0, 0, 1, -1)
        m_y = (1, -1, 0, 0)
        for p in range(4):
            n_i = i + m_x[p]
            n_j = j + m_y[p]
            if self.dfs(n_i, n_j, row, col, board, word[1:]):
                return True
        board[i][j] = temp
        return False


    def exist(self, board: List[List[str]], word: str) -> bool:
        R = len(board)
        C = len(board[0])
        for i in range(R):
            for j in range(C):
                if self.dfs(i, j, R, C, board, word):
                    return True
        return False

s = Solution()
sol = s.exist([["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]], "AAAAAAAAAAAAAAa")
print(sol)