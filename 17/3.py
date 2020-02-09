# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def __init__(self):

        self.ans = 0

    def helper(self, root: TreeNode):
        if not root:
            return 0

        if root.val & 1 == 0:
            if root.left:
                if root.left.left:
                    self.ans += root.left.left.val
                if root.left.right:
                    self.ans += root.left.right.val
            if root.right:
                if root.right.left:
                    self.ans += root.right.left.val
                if root.right.right:
                    self.ans += root.right.right.val

        self.sumEvenGrandparent(root.left)
        self.sumEvenGrandparent(root.right)

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.helper(root)
        return self.ans
