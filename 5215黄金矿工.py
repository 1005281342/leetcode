from typing import List


class Solution:

    def __init__(self):
        self.rt_lst = list()

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        lx = len(grid)
        ly = len(grid[0])
        move = {(0, 1), (0, -1), (1, 0), (-1, 0)}
        s_list = [(i, j, grid[i][j]) for i in range(lx) for j in range(ly) if grid[i][j]]
        for s in s_list:
            stk = [s]
            mark = [[0 for _ in range(ly)] for _ in range(lx)]
            while stk:
                i, j, d = stk.pop()
                self.rt_lst.append(d)
                mark[i][j] = 1
                for a, b in move:
                    a += i
                    b += j
                    if 0 <= a < lx and 0 <= b < ly and grid[a][b] and not mark[a][b]:
                        mark[a][b] = 1

                        stk.append((a, b, d + grid[a][b]))

        return max(self.rt_lst)


if __name__ == '__main__':
    S = Solution()
    res = S.getMaximumGold([[1, 0, 7, 0, 0, 0],
                            [2, 0, 6, 0, 1, 0],
                            [3, 5, 6, 7, 4, 2],
                            [4, 3, 1, 0, 2, 0],
                            [3, 0, 5, 0, 20, 0]])
    print(res)
