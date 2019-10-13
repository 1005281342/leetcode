from typing import List

class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:

        move = {(0, 1), (1, 0), (-1, 0), (0, -1),
                (1, 1), (1, -1), (-1, 1), (-1, -1)}
        lx = 8
        ly = 8

        res = list()
        for a, b in move:
            x, y = king[0] + a, king[1] + b

            while 0 <= x < lx and 0 <= y < ly:
                if [x, y] in queens:
                    res.append([x, y])
                    break
                x += a
                y += b

        return res



