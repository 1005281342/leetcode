from typing import List
from math import inf
from collections import defaultdict


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.dd = dict()

    def dfs(self, r: TreeNode, i=0):
        if r:
            if r.val > self.dd.setdefault(i, -inf):
                self.dd[i] = r.val
            self.dfs(r.left, i + 1)
            self.dfs(r.right, i + 1)

    def largestValues(self, root: TreeNode) -> List[int]:

        self.dfs(root)
        return [i for i in self.dd.values()]
