from typing import List
from collections import Counter


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        cd = Counter(arr)
        length = len(arr)
        at = cd.most_common(length // 2)
        cnt = 0
        for i, m in enumerate(at):
            cnt += m[-1]
            if cnt >= (length // 2):
                return i + 1
        return i + 1
