from typing import List
from collections import Counter


class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:

        res = []
        for q in queries:
            a, b, c = q

            ss = s[a:b + 1]
            if c == 0:
                res.append(ss == "".join(reversed(ss)))
            elif c >= 13:
                res.append(True)
            else:
                d = Counter(ss)
                cc = 0
                for v in d.values():
                    if v % 2:
                        cc += 1
                res.append((cc // 2) <= c)
        return res


# class Solution:
#     def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
#         n = len(s)
#         f = [[0] * 26 for _ in range(n + 1)]
#         for i in range(n):
#             for j in range(26):
#                 f[i + 1][j] = f[i][j]
#             f[i + 1][ord(s[i]) - ord('a')] += 1
#         ans = []
#         for p, q, m in queries:
#             t = 0
#             for i in range(26):
#                 if (f[q + 1][i] - f[p][i]) % 2 != 0:
#                     t += 1
#             ans.append(m >= t // 2)
#         return ans


if __name__ == '__main__':
    S = Solution()
    res = S.canMakePaliQueries("abcda",
                               [[3, 3, 0], [1, 2, 0], [0, 3, 1], [0, 3, 2], [0, 4, 1]])
    print(res)
