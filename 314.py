from typing import List
from collections import defaultdict, deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        dq = deque()
        dq.append((root, 0))
        dd = defaultdict(list)
        while dq:
            r, d = dq.popleft()
            dd[d].append(r.val)
            if r.left:
                dq.append((r.left, d - 1))
            if r.right:
                dq.append((r.right, d + 1))
        return [dd[k] for k in sorted(dd.keys())]
