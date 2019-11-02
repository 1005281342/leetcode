from typing import List
from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cd = Counter(nums)
        ts = [(v, k) for k, v in cd.items()]
        heapq.merge(ts, reverse=True)
        return [v for v, _ in heapq.nlargest(k, ts)]
