from typing import List


class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:

        res = list()
        c, d = toBeRemoved
        for a, b in intervals:
            if b <= c:
                res.append([a, b])
            elif a >= d:
                res.append([a, b])
                return res
            elif a <= c and b <= d:
                res.append([a, c])
                c = b
            elif c <= a and d <= b:
                res.append([d, b])
                return res
            elif a<=c and d <= b:
                res.append([a,c])
                res.append([d,b])
                return res
            elif a >= c and b <= d:
                c = b
        return res
