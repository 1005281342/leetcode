from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        res = sum([sum(v) for v in matrix])
        if res <= 3:
            return res

        a = len(matrix)
        b = len(matrix[0])

        d = 2
        t = min(a, b)
        while d <= t:
            for i in range(a):
                for j in range(b):
                    if (i + d < a) and (j + d < b):
                        x = 0
                        for k in range(d):
                            for kk in range(d):
                                x += matrix[i + k][j + kk]
                        if x == d * d:
                            res += 1

            d += 1
        return res
