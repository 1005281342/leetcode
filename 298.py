from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:

        if not root:
            return 0
        dq = deque()
        dq.append((root, 1))
        max_cnt = 0
        while dq:
            r, c = dq.popleft()
            if c > max_cnt:
                max_cnt = c
            if not r:
                continue
            if r.left:
                if r.val + 1 == r.left.val:
                    dq.append((root.left, c + 1))
                else:
                    dq.append((root.left, 1))
            if r.right:
                if r.val + 1 == r.right.val:
                    dq.append((root.right, c + 1))
                else:
                    dq.append((root.right, 1))

        return max_cnt
