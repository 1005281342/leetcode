from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self.dd = defaultdict(list)

    def bfs(self, r, i=0):
        if r:
            self.dd[i].append(r.val)
            self.bfs(r.left, i + 1)
            self.bfs(r.right, i + 1)

    def deepestLeavesSum(self, root: TreeNode) -> int:
        self.bfs(root)
        return sum(self.dd[max(self.dd.keys())])