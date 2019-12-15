from typing import List
from collections import deque


class Solution:
    def shortestPath(self, A: List[List[int]], k: int) -> int:
        dq = deque()
        m = len(A)
        n = len(A[0])
        if m == 1 and n == 1:
            if k >= A[0][0]:
                return 0
            return -1
        if m == 1:
            if k >= sum(A[0]):
                return n - 1
            return -1
        if n == 1:
            t = 0
            for i in range(m):
                t += A[m][0]
            if k >= t:
                return m - 1
            return -1

        dq.append((0, 1, A[0][1], 1))
        dq.append((1, 0, A[1][0], 1))
        res = 1000000
        s = {(0, 1, k - A[0][1]), (1, 0, k - A[1][0])}
        move = {(1, 0), (0, 1), (0, -1), (-1, 0)}
        while dq:
            x, y, z, d = dq.popleft()
            # if k < 0:
            #     continue
            if x == m - 1 and y == n - 1 and d < res:
                # print(d)
                res = d
                continue
            for a, b in move:
                if 0 <= x + a < m and 0 <= y + b < n:

                    if z + A[x + a][y + b] <= k and (x + a, y + b, z + A[x + a][y + b]) not in s:
                        s.add((x + a, y + b, z + A[x + a][y + b]))
                        dq.append((x + a, y + b, z + A[x + a][y + b], d + 1))
        if res == 1000000:
            res = -1
        return res


if __name__ == '__main__':
    a = [[0, 1, 0, 0, 0, 1, 0, 0],
         [0, 1, 0, 1, 0, 1, 0, 1],
         [0, 0, 0, 1, 0, 0, 1, 0]]
    s = Solution()
    res = s.shortestPath(a, 1)
    print(res)