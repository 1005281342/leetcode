from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        lst0 = []
        lst1 = []
        for i in range(len(grid)):
            for j, v in enumerate(grid[i]):
                if v == 0:
                    lst0.append((i, j))
                else:
                    lst1.append((i, j))

        if len(lst0) == 0 or len(lst1) == 0:
            return -1

        return max([self.md_k(a, lst1) for a in lst0])

    def md(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def md_k(self, zb, lst):
        return min([self.md(zb, b) for b in lst])
