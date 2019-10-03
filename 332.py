from typing import List
from collections import defaultdict, deque

START = "JFK"


class Solution:

    def __init__(self):

        self.dd = defaultdict(list)
        self.rsp = deque()

    def dfs(self, f):
        while self.dd[f]:
            self.dfs(self.dd[f].pop())
        self.rsp.appendleft(f)

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        for k, v in tickets:
            self.dd[k].append(v)

        for k in self.dd:
            self.dd[k].sort(reverse=True)

        self.dfs(START)

        return list(self.rsp)
