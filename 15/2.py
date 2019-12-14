from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        cnt = 0
        intervals.sort(reverse=True)
        for i, c in enumerate(intervals[:-1]):
            for b in intervals[i+1:]:
                if b[0] <= c[0] and b[1] >= c[1]:
                    continue
                cnt += 1
        return cnt
