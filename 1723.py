# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


mod = 10 ** 9 + 7


class Solution:

    def __init__(self):
        self.sm = list()

    def helper(self, r: TreeNode):
        if not r:
            return 0
        t = self.helper(r.left) + self.helper(r.right) + r.val
        self.sm.append(t)
        return t

    def maxProduct(self, root: TreeNode) -> int:
        k = self.helper(root)
        mt = k // 2
        miv, mik = k, -1
        for i in self.sm:
            at = abs(mt - i)
            if at < miv:
                miv = at
                mik = i
        return (mik * (k - mik)) % mod
