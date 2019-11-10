from typing import List
from collections import deque

L = 0
W = 1
MOVE = ((-1, 0), (1, 0), (0, -1), (0, 1))


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        mark_lst = [[False for _ in range(n)] for _ in range(m)]

        count = 0

        for i in range(m):
            for j in range(n):

                if not mark_lst[i][j] and grid[i][j] == L and (i not in (0, m - 1)) and (j not in (0, n - 1)):
                    q = deque()
                    flag = False
                    q.append((i, j))
                    mark_lst[i][j] = True
                    while q:
                        x, y = q.popleft()
                        for a, b in MOVE:
                            a += x
                            b += y

                            if 1 <= a < m - 1 and 1 <= b < n - 1 and not mark_lst[a][b] and grid[a][b] == L:
                                q.append((a, b))
                            if grid[a][b] == L and ((a in (0, m - 1)) or (b in (0, n - 1))):
                                flag = True
                            mark_lst[a][b] = True
                    if flag:
                        count -= 1
                    count += 1
        return count