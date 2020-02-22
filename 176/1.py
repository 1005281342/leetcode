


from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        for m in grid:
            for v in m:
                if v < 0:
                    ans += 1
        return ans  