from typing import List


class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        lr, lc = len(grid), len(grid[0])
        left = [[0] * lc for _ in range(lr)]
        up = [[0] * lc for _ in range(lr)]
        for i in range(lr):
            for j in range(lc):
                if grid[i][j] == 0:
                    left[i][j] = 0
                else:
                    left[i][j] = 1 + (left[i][j - 1] if j >= 1 else 0)

        for j in range(lc):
            for i in range(lr):
                if grid[i][j] == 0:
                    up[i][j] = 0
                else:
                    up[i][j] = 1 + (up[i - 1][j] if i >= 1 else 0)

        ans = 0
        for i in range(lr):
            for j in range(lc):
                if grid[i][j] == 1:
                    tmp = 1
                    l = min(up[i][j], left[i][j])
                    for k in range(1, l + 1):
                        if up[i][j - k + 1] >= k and left[i - k + 1][j] >= k:
                            tmp = max(tmp, k)
                    ans = max(ans, tmp)
        return ans * ans
