from typing import List
from collections import deque, defaultdict

MAX = 10 ** 9 + 7


class Solution:

    def __init__(self):
        self.dd = defaultdict(int)

    def pathsWithMaxScore(self, board: List[str]) -> List[int]:

        a = len(board)
        nums = [['0' for _ in range(a)] for _ in range(a)]
        for i, v in enumerate(board):
            for j, c in enumerate(v):
                nums[i][j] = c
        move = {
            (-1, 0),
            (0, -1),
            (-1, -1)
        }
        dq = deque()
        dq.append((a - 1, a - 1, 0))
        while dq:
            x, y, d = dq.pop()
            for cx, cy in move:
                cx += x
                cy += y
                if 0 <= cx <= a and 0 <= cy <= a:
                    if nums[cx][cy] == 'X':
                        continue
                    if nums[cx][cy] == 'E':
                        self.dd[d] += 1
                        break
                    if 9 < d < 2*a - cx - cy:
                        break
                    td = (d + int(nums[cx][cy])) % MAX
                    dq.append((cx, cy, td))
        try:
            hk = max(self.dd.keys())
        except:
            return [0, 0]
        return [hk, self.dd[hk]]


if __name__ == '__main__':
    S = Solution()
    res = S.pathsWithMaxScore(["E914412261","8435789189","923667666X","2859957657","2327X3559X","8822118927","4562991X7X","582X552335","X814712836","188273119S"])
    print(res)