class Solution(object):
    def swimInWater(self, grid):
        N = len(grid)
        l, r = grid[0][0], N * N - 1

        def reachable(T):
            bfs = [(0, 0)]
            seen = set((0, 0))
            for x, y in bfs:
                if grid[x][y] <= T:
                    if x == y == N - 1: return True
                    for i, j in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                        if 0 <= x + i < N and 0 <= y + j < N and (x + i, y + j) not in seen:
                            seen.add((x + i, y + j))
                            bfs.append((x + i, y + j))
            return False

        while l < r:
            m = (l + r) / 2
            if reachable(m): r = m
            else: l = m + 1
        return r

s = Solution()
sol = s.swimInWater([[3,2],[0,1]])
print(sol)