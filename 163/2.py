# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class FindElements:

    def __init__(self, root: TreeNode):
        # self.root = root
        self.lst = list()
        self.tm = 10**4 + 10
        self.fs(root)
        for j in range(len(self.lst)):
            if self.lst[j] is not None:
                self.lst[j] = j


    def fs(self, r: TreeNode):
        dq = deque()
        dq.append(r)
        while dq and self.tm:
            self.tm -= 1
            x = dq.popleft()
            if x is None:
                self.lst.append(None)
                dq.append(None)
                dq.append(None)
            if x:
                self.lst.append(x.val)
                dq.append(x.left)
                dq.append(x.right)

    # def helper(self, v) -> TreeNode:
    #     if v is not None:
    #         r = TreeNode(v)
    #         if v*2+1 < len(self.t) and self.t[2*v+1]:
    #             r.left = TreeNode(self.t[2*v+1])
    #         if v * 2 + 2 < len(self.t) and self.t[2 * v + 2]:
    #             r.right = TreeNode(self.t[2 * v + 2])
    #         return r
    #     return

    def find(self, target: int) -> bool:

        if target < len(self.lst):
            return bool(self.lst[target])
        return False

        # return target in self.lst

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
