from typing import List
from collections import defaultdict


class Solution:
    def countServers(self, t: List[List[int]]) -> int:
        rs = set()
        dd = defaultdict(set)
        dd2 = defaultdict(set)

        for i, x in enumerate(t):
            for j, v in enumerate(x):
                if v == 1:
                    dd[i].add((i, j))
                    dd2[j].add((i, j))
        #
        # for a, b in grid:
        #     dd[a].add((a, b))
        #     dd2[b].add((a, b))

        for a in dd.values():
            if len(a) >= 2:
                rs |= a

        for a in dd2.values():
            if len(a) >= 2:
                rs |= a

        return len(rs)
