from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        ans = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]

        xx = len(mat)
        yy = len(mat[0])

        for ti in range(xx):
            y = 0
            t = list()
            i = ti
            while i < xx and y < yy:
                t.append(mat[i][y])
                i += 1
                y += 1
            if t:
                t.sort()
                y = 0
                for v in t:
                    ans[ti][y] = v
                    ti += 1
                    y += 1

        for ti in range(yy):
            x = 0
            t = list()
            i = ti
            while i < yy and x < xx:
                t.append(mat[x][i])
                i += 1
                x += 1
            if t:
                t.sort()
                x = 0
                for v in t:
                    ans[x][ti] = v
                    ti += 1
                    x += 1
        return ans