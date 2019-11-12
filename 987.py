# Definition for a binary tree node.
from typing import List
from collections import defaultdict


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self.dd = defaultdict(list)

    def fs(self, r: TreeNode, x=0, y=0):
        if r:
            self.dd[(x, y)].append(r.val)
            self.fs(r.left, x - 1, y+1)
            self.fs(r.right, x + 1, y+1)

    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:

        self.fs(root, 0)
        ans = []
        keys = sorted(self.dd.keys())

        for k, v in self.dd.items():
            self.dd[k] = sorted(v)

        tlst = []
        t = keys[0][0]
        for k in keys:
            x, _ = k
            if x == t:
                tlst.extend(self.dd[k])
            else:
                ans.append(tlst)
                t = x
                tlst = self.dd[k]
        if tlst:
            ans.append(tlst)
        return ans