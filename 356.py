from typing import List
from collections import defaultdict


class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:

        if not points:
            return True
        dd = defaultdict(set)
        for x, y in points:
            dd[y].add(x)
        ts = set()
        for v in dd.values():
            if len(v) % 2 and len(v) != 1 and 0 not in v:
                return False
            elif len(v) % 2 and 0 in v and sum(v) != 0:
                return False
            ts.add(sum(v) / len(v))
        return len(ts) == 1
