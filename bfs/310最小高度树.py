from typing import List
from collections import defaultdict


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        e = defaultdict(set)  # 字典初始化为集合
        for i, j in edges:
            e[i].add(j)  # 把边哈希化，方便调用
            e[j].add(i)
        q = {i for i in e if len(e[i]) == 1}  # 建立初始宽搜队列，长度为1时代表只连接一个点
        while n > 2:
            t = set()  # 临时队列
            for i in q:
                j = e[i].pop()  # 把连接点取出
                e[j].remove(i)  # 连接是双向的，所以要删除关系
                if len(e[j]) == 1:  # 更新后，如果长度为1时则加入下一个轮队列
                    t.add(j)
                n -= 1  # 删除计数
            q = t
        return list(q)


# class Solution:
#     def __init__(self):
#         self.d = dict()
#
#     def add_kv(self, a, b):
#         if self.d.get(a):
#             self.d[a].append(b)
#         else:
#             self.d[a] = [b]
#         if self.d.get(b):
#             self.d[b].append(a)
#         else:
#             self.d[b] = [a]
#
#     def arr2dict(self, edges: List[List[int]]):
#         for a, b in edges:
#             self.add_kv(a, b)
#
#     def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
#         if not edges or not edges[0]:
#             return []
#         self.arr2dict(edges)
#         tmp = list()
#         c = inf
#         for i in range(n):
#             dd = defaultdict(list)
#             q = deque()
#             q.append(i)
#             s = set()
#             while q:
#                 k = q.popleft()
#                 if k in s:
#                     continue
#                 s.add(k)
#                 for cc in self.d.get(k):
#                     if cc in s:
#                         continue
#                     dd[k].append(cc)
#                     q.append(cc)
#                 # dd[k].extend(self.d.get(k))
#                 # q.extend(self.d.get(k))
#
#             if not dd:
#                 continue
#
#             ld = len(dd.keys())
#             print(i, ld)  # 缺少合并过程
#             print(dd)
#             if ld < c:
#                 c = ld
#                 tmp = [i]
#             elif ld == c:
#                 tmp.append(i)
#
#         return tmp


if __name__ == '__main__':
    S = Solution()
    req = [[0, 1], [0, 2], [0, 3], [3, 4], [4, 5]]

    n = 6
    res = S.findMinHeightTrees(n, req)
    print(res)
