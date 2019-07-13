# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self.lst = []
        self.Max = 0

    def print_root(self, root: TreeNode):
        if root is None:
            return
        # print(root.val)
        self.lst.append(root.val or -1)  # -1 为空节点
        self.print_root(root.left)
        self.print_root(root.right)

    def maximumAverageSubtree(self, root: TreeNode) -> float:
        self.print_root(T)
        print(self.lst)

        index = len(self.lst)
        #
        self.Max = self.lst[index:].append(self.lst[0])
        pass

        return 0


T = TreeNode(5)
T.left = TreeNode(None)
T.right = TreeNode(1)
S = Solution()
# S.print_root(T)
S.maximumAverageSubtree(T)
