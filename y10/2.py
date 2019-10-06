# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self.lst1 = set()
        self.lst2 = set()

    def qx(self, r: TreeNode, state=True):
        if r:
            self.qx(r.left, state)
            if state:
                self.lst1.add(r.val)
            else:
                self.lst2.add(r.val)
            self.qx(r.right, state)

    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:

        self.qx(root1)
        self.qx(root2, False)

        # if not self.lst1 or not self.lst2:
        #     return False
        print(self.lst1)
        print(self.lst2)

        for i in self.lst2:
            if target - i in self.lst1:
                return True

        return False
