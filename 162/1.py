from typing import List


class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        t = [[0 for _ in range(m)] for _ in range(n)]

        for r, c in indices:

            for i in range(n):
                for j in range(m):
                    if i == r:
                        t[r][j] += 1
                    if j == c:
                        t[i][c] += 1

        cnt = 0
        for i in range(n):
            for j in range(m):
                if t[i][j] % 2:
                    cnt += 1
        return cnt