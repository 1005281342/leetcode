from typing import List
from collections import defaultdict


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dd = defaultdict(list)

        for i, v in enumerate(nums):
            dd[v].append(i)

        for v in dd.values():
            for j in range(len(v) - 1):
                if v[j + 1] - v[j] <= k:
                    return True
        return False
