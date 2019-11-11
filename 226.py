# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def fs(self, r: TreeNode):
        if r:
            r.left, r.right = r.right, r.left
            self.fs(r.left)
            self.fs(r.right)

    def invertTree(self, root: TreeNode) -> TreeNode:
        self.fs(root)
        return root
