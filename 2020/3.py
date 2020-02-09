from typing import List
from collections import deque, defaultdict


class Solution:
    def happy(self, n: int, roads: List[List[int]], codes: List[str]) -> str:
        start = 11
        end = 0
        ans = ""
        dd = defaultdict(set)
        for a, b in roads:
            dd[a].add(b)
            dd[b].add(a)

