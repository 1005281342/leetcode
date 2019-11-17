from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        m = len(grid)
        n = len(grid[0])
        t = m*n - k%(m*n)

        tmp = [grid[i][j] for i in range(m) for j in range(n)]
        print(tmp)

        new = tmp[t:] + tmp[:t]

        return [new[i*m: i*m+m] for i in range(n)]

if __name__ == '__main__':
    pass
