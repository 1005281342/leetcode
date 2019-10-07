from typing import List


# from collections import defaultdict


# class Solution:
#     def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
#         dd = defaultdict(list)
#         for i, w in enumerate(words):
#             dd[w].append(i)
#
#         lst = list()
#         for a in dd[word1]:
#             for b in dd[word2]:
#                 lst.append(abs(a-b))
#
#         return min(lst)

class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        a, b = None, None
        res = len(words)
        for i, w in enumerate(words):
            if w == word1:
                a = i
            elif w == word2:
                b = i
            if a is not None and b is not None:
                res = min(res, abs(a - b))
        return res
