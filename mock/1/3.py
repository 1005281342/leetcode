from typing import List
from collections import Counter


class DSU:
    def __init__(self, n):
        self.p = range(n)
        self.sz = [1] * n

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr
        self.sz[yr] += self.sz[xr]

    def size(self, x):
        return self.sz[self.find(x)]


class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:

        dsu = DSU(len(graph))

        for j, row in enumerate(graph):
            for i in range(j):
                if row[i]:
                    dsu.union(i, j)

        count = Counter(dsu.find(u) for u in initial)
        ans = (-1, min(initial))
        for node in initial:
            root = dsu.find(node)
            if count[root] == 1:
                if dsu.size(root) > ans[0] or (dsu.size(root) == ans[0] and node < ans[1]):
                    ans = dsu.size(root), node
        return ans[1]