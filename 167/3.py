from typing import List


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m = len(mat)
        n = len(mat[0])
        t = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        # 计算前缀和
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                t[i][j] = t[i][j - 1] + t[i - 1][j] - t[i - 1][j - 1] + mat[i - 1][j - 1]

        k = 0
        for i in range(m):
            for j in range(n):
                k = 1
                while i + k <= m and j + k <= n:
                    if t[i + k][j + k] - t[i + k][j] - t[i][j + k] + t[i][j] <= threshold:
                        k += 1
                    else:
                        break
        k -= 1
        return max(0, k)
