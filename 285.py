# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self.lst = list()

    def inorder(self, r: TreeNode):
        if r:
            self.inorder(r.left)
            self.lst.append(r)
            self.inorder(r.right)

    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        self.inorder(root)
        i = self.lst.index(p)
        return self.lst[i + 1] if i + 1 < len(self.lst) else None
