"""
裸题，子矩阵求和
容斥原理
"""

from typing import List
from typing import Optional

class NumMatrix:
    def get_sum(self, row, col):
        if row >= 0 and col >= 0:
            return self.sum[row][col]
        return 0

    def __init__(self, matrix: List[List[int]]):
        self.sum = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            row_sum = [0 for _ in range(len(matrix[0]))]
            for j in range(len(matrix[0])):
                cur = matrix[i][j]
                if j > 0:
                    cur += row_sum[j-1]
                row_sum[j] = cur
                pre_row_sum = cur
                if i > 0:
                    pre_row_sum += self.sum[i-1][j]
                self.sum[i][j] = pre_row_sum
        print(self.sum)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.get_sum(row2, col2) - self.get_sum(row1-1, col2) - self.get_sum(row2, col1-1) + self.get_sum(row1-1, col1-1)

m = NumMatrix(
[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]
)

query = [[2,1,4,3],[1,1,2,2],[1,2,2,4]]
for q in query:
    print(m.sumRegion(q[0], q[1], q[2], q[3]))