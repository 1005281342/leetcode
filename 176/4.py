from typing import List

class Solution:
    def isPossible(self, target: List[int]) -> bool:

        ma = max(target)
        s = set()
        x = [1] * len(target)


