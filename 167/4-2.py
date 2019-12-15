from typing import List
from math import inf
from collections import deque


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        ans = inf

        start = (0, 0, 0, 0)
        move = {(0, 1), (0, -1), (1, 0), (-1, 0)}
        dq = deque()
        dq.append(start)
        m = len(grid)
        n = len(grid[0])
        s = {(0, 0, 0), }
        while dq:

            a, b, z, d = dq.popleft()
            if a == m - 1 and b == n - 1 and z <= k and d < ans:
                return d

            for x, y in move:
                x += a
                y += b
                if 0 <= x < m and 0 <= y < n and z + grid[x][y] <= k and (x, y, z + grid[x][y]) not in s:
                    s.add((x, y, z + grid[x][y]))
                    dq.append((x, y, z + grid[x][y], d + 1))

        if ans == inf:
            return -1
