from typing import List


# from math import gcd


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        for i in range(len(points) - 1):
            a = abs(points[i + 1][1] - points[i][1])
            b = abs(points[i + 1][0] - abs(points[i][0]))
            d1 = min(a, b)
            res += a + b - d1
        return res