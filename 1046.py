from typing import List
import heapq


class Solution:
    # 利用存入 相反数 维护最小堆， 弹出后再还原相反数即得最大堆目标数
    def lastStoneWeight(self, stones: List[int]) -> int:
        t = [-s for s in stones]
        t = heapq.heapify(t)
        while len(t) > 1:
            y = heapq.heappop(t)
            x = heapq.heappop(t)
            if x == y:
                continue
            t.append(y-x)

        return -t[0] if t else 0

