# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def __init__(self):
        self.ans = list()

    def helper(self, r: TreeNode):

        if r:
            self.ans.append(r.val)
            self.helper(r.left)
            self.helper(r.right)


    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        self.helper(root1)
        self.helper(root2)
        return sorted(self.ans)