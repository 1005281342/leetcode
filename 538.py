# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def __init__(self):
        self.num = 0

    def convertBST(self, root: TreeNode) -> TreeNode:

        """
        遍历顺序：右->中->左
        :param root:
        :return:
        """

        if root:
            self.convertBST(root.right)
            root.val += self.num
            self.num = root.val
            self.convertBST(root.left)
            return root
        return None
