"""
# Definition for a Node.

"""
from collections import defaultdict


class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def __init__(self):
        self.dd = defaultdict(list)

    def dfs(self, r: 'Node', i=0):
        if r:
            self.dd[i].append(r.val)
            for c in r.children:
                self.dfs(c, i + 1)

    def maxDepth(self, root: 'Node') -> int:
        self.dfs(root)
        return len(self.dd.keys())
