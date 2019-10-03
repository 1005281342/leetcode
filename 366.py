from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [[root.val]]

        rs = []
        while True:
            rs.append(self.delete(root))
            if root.left is None and root.right is None:
                rs.append([root.val])
                break
        return rs

    def delete(self, root: TreeNode):
        rs = []
        list1 = [(None, None, root)]
        while list1:
            f_node, pos, now_node = list1.pop(0)
            if now_node.left is not None:
                list1.append((now_node, 'left', now_node.left))
            if now_node.right is not None:
                list1.append((now_node, 'right', now_node.right))
            if now_node.left is None and now_node.right is None:
                if pos == 'left':
                    f_node.left = None
                elif pos == 'right':
                    f_node.right = None
                rs.append(now_node.val)
        return rs
