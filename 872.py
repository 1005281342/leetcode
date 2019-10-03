# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        rsp1 = []
        if root1:
            stk1 = [root1]
            while stk1:
                k = stk1.pop()
                if k:
                    if k.left and k.right:
                        stk1.append(k.left)
                        stk1.append(k.right)
                    else:
                        rsp1.append(k.val)

        rsp2 = []
        if root2:
            stk1 = [root2]
            while stk1:
                k = stk1.pop()
                if k:
                    if k.left and k.right:
                        stk1.append(k.left)
                        stk1.append(k.right)
                    else:
                        rsp2.append(k.val)
        print(rsp1)
        print(rsp2)

        return rsp1 == rsp2
