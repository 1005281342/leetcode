from collections import defaultdict, deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self.dd = defaultdict(list)

    def dfs(self, r: TreeNode, i=0):
        if r:
            self.dd[i].append(r.val)
            self.dfs(r.left, i + 1)
            self.dfs(r.right, i + 1)

    def findBottomLeftValue(self, root: TreeNode) -> int:

        self.dfs(root)
        return self.dd[list(self.dd.keys())[-1]][0]
