class Solution:

    def __init__(self):
        self.ans = None

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        self.ans = 0

        def dfs(start, presum):
            x, y = start
            presum += grid[x][y]
            self.ans = max(self.ans, presum)
            for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    dfs((nx, ny), presum)
                    visited.remove((nx, ny))

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    visited = set()
                    visited.add((i, j))
                    dfs((i, j), 0)
        return self.ans

