
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        lst = self.Print(root)
        d = dict()
        for i, a in enumerate(lst):
            h = sum(a)
            if d.get(h):
                continue
            else:
                d[h] = i+1
        return d[max(d.keys())]

    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        queue = [pRoot]
        outList = []
        while queue:
            res = []
            nextQueue = []
            for point in queue:  # 这里再遍历每一层
                res.append(point.val)
                if point.left:
                    nextQueue.append(point.left)
                if point.right:
                    nextQueue.append(point.right)
            outList.append(res)
            queue = nextQueue  # 这一步很巧妙，用当前层覆盖上一层
        return outList

    def PrintFromTopToBottom(self, root):
        # write code here
        outList = []
        queue = [root]
        while queue != [] and root:
            outList.append(queue[0].val)
            print(outList)
            if queue[0].left != None:
                queue.append(queue[0].left)
            if queue[0].right != None:
                queue.append(queue[0].right)
            queue.pop(0)
        return outList
