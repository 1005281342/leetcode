from typing import List
from collections import defaultdict, deque

"""
拓扑排序
    无环 有向图
"""


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dd = defaultdict(set)

        # 领接表
        for k, v in prerequisites:
            dd[k].add(v)

        # 入度
        rd = [0] * numCourses
        for vs in dd.values():
            for v in vs:
                rd[v] += 1

        dq = deque()
        for i, v in enumerate(rd):
            if v == 0:
                dq.append(i)

        ans = list()
        while dq:
            x = dq.pop()
            ans.append(x)
            for tv in dd[x]:
                rd[tv] -= 1
                if rd[tv] == 0:
                    dq.append(tv)
        return ans if len(ans) == numCourses else []
