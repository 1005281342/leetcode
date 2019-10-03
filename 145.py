from collections import deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return list()
        rsp, stk = deque(), [root, ]
        while stk:
            r = stk.pop()
            if r:
                stk.append(r.left)
                stk.append(r.right)
                rsp.appendleft(r.val)
        return list(rsp)
