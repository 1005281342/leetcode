from typing import List
from collections import defaultdict, deque


class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:

        dd = defaultdict(list)
        tq = dict()
        for i, region in enumerate(regions):

            for v in region[1:]:
                dd[v].append(region[0])
                dd[v].append(v)
            tq[region[0]] = i

        dq = deque(dd[region1])
        t1 = set()
        while dq:
            a = dq.popleft()
            if a not in t1:
                t1.add(a)
                dq.extend(dd[a])
        dq = deque(dd[region2])
        t2 = set()
        while dq:
            a = dq.popleft()
            if a not in t2:
                t2.add(a)
                dq.extend(dd[a])
        t = t1 & t2
        if len(t) == 1:
            return list(t)[0]

        x = -1
        res = None
        for c in t:
            if tq[c] > x:
                res = c
                x = tq[c]
        return res
